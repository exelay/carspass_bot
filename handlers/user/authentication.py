import json
import requests
from aiogram import types

from loader import dp
from messages import MESSAGES
from utils.db_api.commands import add_user


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def auth_handler(message: types.Message):
    id_ = message.from_user.id
    phone = message.contact.phone_number
    response = requests.get(
        "https://app.carspass.ru/webhook/telegram",
        params={"phone": phone}
    )
    response_json = json.loads(response.text)
    if response.status_code == 200:
        code = response_json['code']
        await message.answer(MESSAGES['auth_success'].format(code))
        await add_user(id_, phone, code)
    else:
        await message.answer(MESSAGES['auth_fail'])
