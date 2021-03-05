from urllib import parse
from loguru import logger
from fastapi import APIRouter

from loader import db, dp
from utils.notify_admins import error_notify

router = APIRouter()


async def make_query_msg(link):
    link_params = parse.parse_qs(parse.urlsplit(link).query)
    query_params = {k: v[0] for k, v in link_params.items()}

    brand, model = query_params.get('brand').title(), query_params.get('model').title()
    price_min, price_max = query_params.get('price_min'), query_params.get('price_max')
    city = query_params.get('city')

    price_min = f' от {price_min}₽' if price_min else ''
    price_max = f' до {price_max}₽' if price_max else ''
    city = f' в городе {city}' if city else ''

    return f"{brand} {model}{city}{price_min}{price_max}"


@router.post('/notify', tags=['notification'])
async def ad_notification(phone: str, link: str, count: int):
    """
    A **POST** method that notify user about new ad for user's search request.
    """
    try:
        user = db.select_user(phone=phone)
        if not user:
            return {'Error': f'User with phone {phone} not found.'}
        user_id = user[0]
        query_msg = await make_query_msg(link)
        message = (
            f'🧨Появилось новое объявление по твоему запросу:\n'
            f'{query_msg}\n'
            f'Всего объявлений: {count}.\n'
            f'<a href="{link}">Проверить</a>'
        )
        await dp.bot.send_message(user_id, message)
        return {'status': 'OK'}
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")


@router.post('/change_password', tags=['change_password'])
async def change_password(user_id: str, link: str):
    """
    A **POST** method that send link for change password.
    """
    try:
        message = (
            f'<a href="{link}">Сменить пароль</a>'
        )
        await dp.bot.send_message(user_id, message)
        return {'status': 'OK'}
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")
        return {'Error': f'User with id {user_id} did not start a bot.'}
