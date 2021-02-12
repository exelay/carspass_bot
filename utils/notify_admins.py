from loguru import logger
from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    message = "Бот запущен!"

    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, message)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")


async def error_notify(dp: Dispatcher, error):
    message = f"Что-то пошло не так! Ошибка: {error}"

    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, message)
        except Exception as err:
            logger.error(f"Message is not delivered. Exception: {err}")
