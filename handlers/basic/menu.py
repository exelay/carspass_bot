from aiogram.types import CallbackQuery

from loader import dp
from keyboards import menu_markup


@dp.callback_query_handler(text='menu')
async def show_menu(callback: CallbackQuery):
    await callback.message.answer("Меню", reply_markup=menu_markup)
