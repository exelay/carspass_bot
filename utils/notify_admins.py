from loguru import logger
from aiogram import Dispatcher, types

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher, db):
    text = (
        "#for_admins\n"
        "Бот запущен! Всего пользователей: {}"
    )
    for admin in ADMINS:
        try:
            count = db.count_users()[0]
            await dp.bot.send_message(admin, text.format(count))
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")


async def error_notify(dp: Dispatcher, error):
    text = (
        "#for_admins\n"
        f"Что-то пошло не так! Ошибка: {error}"
    )
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")


async def new_user_notify(dp: Dispatcher, message: types.Message):
    name = message.from_user.first_name
    user_id = message.from_user.id
    text = (
        "#for_admins\n"
        f"Авторизовался новый пользователь:\n{name} | {user_id}"
    )
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")
