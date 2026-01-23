# Chatbot Server

Это Flask-приложение для сервера чатбота, который может принимать сообщения от пользователей и возвращать ответы. Проект включает в себя простую систему хранения истории переписки и поддерживает мультипользовательские беседы.

## Функциональность

- `/` - Главная страница с информацией о статусе сервера
- `/chat` - Основной эндпоинт для взаимодействия с чатботом
- `/history` - Получение истории переписки
- `/reset` - Сброс истории переписки

## Установка и запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите сервер:
```bash
python app.py
```

Сервер будет запущен на порту 5000 (или на порту из переменной окружения PORT).

## Использование API

### Отправка сообщения чатботу

```
POST /chat
Content-Type: application/json

{
  "message": "Привет!",
  "user_id": "optional_user_id"
}
```

Ответ:
```json
{
  "status": "success",
  "user_message": "Привет!",
  "bot_response": "Hello! How can I help you today?",
  "conversation_id": "optional_user_id"
}
```

### Получение истории переписки

```
GET /history?user_id=test_user
```

Или

```
POST /history
Content-Type: application/json

{
  "user_id": "test_user"
}
```

### Сброс истории переписки

```
POST /reset
Content-Type: application/json

{
  "user_id": "test_user"
}
```

## Зависимости

- Flask - веб-фреймворк
- Flask-CORS - поддержка CORS
- Requests - HTTP библиотека
- Gunicorn - WSGI сервер для продакшена