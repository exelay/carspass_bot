from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_markup = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Меню", callback_data='menu'),
    InlineKeyboardButton("Вернуться на сайт", url='https://app.carspass.ru/')
)
