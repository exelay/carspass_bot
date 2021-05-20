# Telegram-бот уведомлений от carspass.ru
## Подготовка
### Настройка среды
`python -m venv venv`

`source venv/bin/activate`
### Установка зависимостей
`pip install -r requirements.txt`

### Переменные окружения
`cp .env.dist .env`

Открыть .env предпочитаемым текстовым редактором. В переменную `TOKEN` вставить токен Telegram. В переменной `ADMINS` перечислить telegram-id администраторов через запятую.
## Запуск
### TelegramBot сервер
`python app.py`
### API уведомлений
`python api_main.py`