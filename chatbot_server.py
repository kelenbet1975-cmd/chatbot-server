from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simple in-memory storage for conversation history
conversation_history = {}

@app.route('/')
def home():
    """Home route to check if server is running"""
    return jsonify({
        "status": "success",
        "message": "Chatbot server is running",
        "endpoints": {
            "/chat": "Send a message to the chatbot",
            "/history": "Get conversation history",
            "/reset": "Reset conversation history"
        }
    })

@app.route('/chat', methods=['POST'])
def chat():
    """
    Main endpoint to interact with the chatbot
    Expects JSON with 'message' field
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Message field is required"}), 400
        
        user_message = data['message']
        user_id = data.get('user_id', 'default_user')  # Allow per-user history
        
        # Initialize conversation history for user if not exists
        if user_id not in conversation_history:
            conversation_history[user_id] = []
        
        # Add user message to history
        conversation_history[user_id].append({"role": "user", "message": user_message})
        
        # Generate bot response (simple echo for now, can be replaced with AI model)
        bot_response = generate_bot_response(user_message, conversation_history[user_id])
        
        # Add bot response to history
        conversation_history[user_id].append({"role": "bot", "message": bot_response})
        
        return jsonify({
            "status": "success",
            "user_message": user_message,
            "bot_response": bot_response,
            "conversation_id": user_id
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_bot_response(user_message, history):
    """
    Function to generate bot response based on user message
    This is a simple implementation - can be replaced with more sophisticated logic
    """
    user_message_lower = user_message.lower()
    
    # Simple rule-based responses
    if any(greeting in user_message_lower for greeting in ['hello', 'hi', 'hey', 'привет']):
        return "Hello! How can I help you today?"
    elif any(bye in user_message_lower for bye in ['bye', 'goodbye', 'пока', 'до свидания']):
        return "Goodbye! Have a great day!"
    elif 'help' in user_message_lower or 'помощь' in user_message_lower:
        return "I'm here to help! You can ask me questions or just chat with me."
    elif 'name' in user_message_lower:
        return "I'm a friendly chatbot created to assist you!"
    elif '?' in user_message:
        return "That's an interesting question! Can you tell me more about it?"
    else:
        # Echo back with slight variation if no specific rule matches
        return f"I received your message: '{user_message}'. How else can I assist you?"

@app.route('/history', methods=['GET', 'POST'])
def get_history():
    """
    Get conversation history
    Accepts user_id in query parameter or request body
    """
    try:
        # Check both query params and request body for user_id
        user_id = request.args.get('user_id', 'default_user')
        
        if request.is_json:
            data = request.get_json()
            user_id = data.get('user_id', user_id)
        
        history = conversation_history.get(user_id, [])
        
        return jsonify({
            "status": "success",
            "user_id": user_id,
            "history": history,
            "count": len(history)
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset_history():
    """
    Reset conversation history for a user
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'default_user')
        
        if user_id in conversation_history:
            del conversation_history[user_id]
        
        return jsonify({
            "status": "success",
            "message": f"Conversation history for user {user_id} has been reset"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)