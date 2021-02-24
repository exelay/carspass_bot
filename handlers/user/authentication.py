import json
import sqlite3
import requests
from loguru import logger
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db
from utils.notify_admins import new_user_notify, error_notify
from messages import MESSAGES


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def auth_handler(message: types.Message):
    try:
        id_ = message.from_user.id
        phone = message.contact.phone_number
        response = requests.get(
            "https://app.carspass.ru/webhook/telegram",
            params={"phone": phone}
        )
        response_json = json.loads(response.text)
        if response.status_code == 200:
            code = response_json['code']
            try:
                db.add_user(id_, phone, code)
                await new_user_notify(dp, message)
            except sqlite3.IntegrityError:
                pass
            await message.answer(MESSAGES['auth_success'].format(code))
        else:
            await message.answer(MESSAGES['auth_fail'])
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")


@dp.message_handler(Command('auth'))
async def auth_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton("🚨Авторизоваться🚨", request_contact=True)
        ],
        [
            types.KeyboardButton("💵Подтвердить оплату💵")
        ]
    ], one_time_keyboard=True, resize_keyboard=True)
    await message.answer("Кнопка авторизации ниже.", reply_markup=markup)
