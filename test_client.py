import requests
import json

BASE_URL = "http://localhost:5000"

def test_chatbot():
    print("Тестирование чатбота...")
    
    # Тест главной страницы
    print("\n1. Проверка главной страницы:")
    response = requests.get(BASE_URL + "/")
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Тест отправки сообщения
    print("\n2. Отправка сообщения чатботу:")
    payload = {
        "message": "Привет!",
        "user_id": "test_user_1"
    }
    response = requests.post(BASE_URL + "/chat", json=payload)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Второе сообщение от того же пользователя
    print("\n3. Второе сообщение от того же пользователя:")
    payload = {
        "message": "Как дела?",
        "user_id": "test_user_1"
    }
    response = requests.post(BASE_URL + "/chat", json=payload)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Сообщение от другого пользователя
    print("\n4. Сообщение от другого пользователя:")
    payload = {
        "message": "Пока!",
        "user_id": "test_user_2"
    }
    response = requests.post(BASE_URL + "/chat", json=payload)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Получение истории первого пользователя
    print("\n5. Получение истории первого пользователя:")
    params = {"user_id": "test_user_1"}
    response = requests.get(BASE_URL + "/history", params=params)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Получение истории второго пользователя
    print("\n6. Получение истории второго пользователя:")
    params = {"user_id": "test_user_2"}
    response = requests.get(BASE_URL + "/history", params=params)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Сброс истории первого пользователя
    print("\n7. Сброс истории первого пользователя:")
    payload = {"user_id": "test_user_1"}
    response = requests.post(BASE_URL + "/reset", json=payload)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    # Проверка, что история первого пользователя очищена
    print("\n8. Проверка, что история первого пользователя очищена:")
    params = {"user_id": "test_user_1"}
    response = requests.get(BASE_URL + "/history", params=params)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    test_chatbot()