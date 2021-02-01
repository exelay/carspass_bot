import json
import requests
from aiogram import types

from loader import dp
from messages import MESSAGES


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def auth_handler(message: types.Message):
    phone_number = message.contact.phone_number
    response = requests.get(
        "https://app.carspass.ru/webhook/telegram",
        params={"phone": phone_number}
    )
    response_json = json.loads(response.text)
    if response.status_code == 200:
        code = response_json['code']
        await message.answer(MESSAGES['auth_success'].format(code))
    else:
        await message.answer(MESSAGES['auth_fail'])
