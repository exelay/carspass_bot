from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from messages import MESSAGES


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup().add(
        types.KeyboardButton("🚨Авторизоваться🚨", request_contact=True)
    )
    user_name = message.from_user.first_name
    text = MESSAGES['hello'].format(user_name)
    await message.answer(text, reply_markup=markup)
