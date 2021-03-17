from typing import Optional, List
from urllib import parse
from loguru import logger

from fastapi import APIRouter, Body

from loader import dp
from utils.notify_admins import error_notify
from pydantic import BaseModel


router = APIRouter()


class Filters(BaseModel):
    brand: str
    model: str
    city: str
    sites: List[str]
    radius: Optional[str] = None
    price_min: Optional[str] = None
    price_max: Optional[str] = None
    year_min: Optional[str] = None
    year_max: Optional[str] = None
    v_min: Optional[str] = None
    v_max: Optional[str] = None
    transmission: Optional[str] = None
    car_body: Optional[str] = None
    steering_w: Optional[str] = None
    latest_ads: Optional[str] = None


class Item(BaseModel):
    brand: str
    model: str
    year: str
    title: str
    link: str
    img_link: str
    price: str


class Notification(BaseModel):
    tg_id: str
    count: str
    filters: Filters
    items: List[Item]


async def make_query_msg(filters):

    price_min = f' от {filters.price_min}₽' if filters.price_min else ''
    price_max = f' до {filters.price_max}₽' if filters.price_max else ''
    city = f' в городе {filters.city}' if filters.city else ''

    return f"{filters.brand} {filters.model}{city}{price_min}{price_max}"


@router.post('/notify', tags=['notification'])
async def ad_notification(notification: Notification):
    """
    A **POST** method that notify user about new ad for user's search request.
    """
    try:
        count = notification.count
        tg_id = notification.tg_id
        query_msg = await make_query_msg(notification.filters)
        message = (
            f'🧨Появились новые объявления по твоему запросу:\n'
            f'<b>{query_msg}</b>\n'
            f'Всего объявлений: {count}.\n'
            '📜 Новые объявления:\n'
        )
        for item in notification.items:
            message += f'🔸 <a href="{item.link}">{item.title}</a>\n'
        await dp.bot.send_message(tg_id, message)
        return {'status': 'OK'}
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")


@router.post('/change_password', tags=['change_password'])
async def change_password(tg_id: str, link: str):
    """
    A **POST** method that send link for change password.
    """
    try:
        message = (
            f'<a href="{link}">Сменить пароль</a>'
        )
        await dp.bot.send_message(tg_id, message)
        return {'status': 'OK'}
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")
        return {'Error': f'User with id {tg_id} did not start a bot.'}
