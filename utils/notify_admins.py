from loguru import logger
from aiogram import Dispatcher, types

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher, db):
    text = "Бот запущен! Всего пользователей: {}"

    for admin in ADMINS:
        try:
            count = db.count_users()[0]
            await dp.bot.send_message(admin, text.format(count))
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")


async def error_notify(dp: Dispatcher, error):
    text = f"Что-то пошло не так! Ошибка: {error}"

    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")


async def new_user_notify(dp: Dispatcher, message: types.Message):
    name = message.from_user.first_name
    phone = message.contact.phone_number
    text = f"Авторизовался новый пользователь:\n{name} | {phone}"

    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")
