from fastapi import APIRouter

from loader import db, dp

router = APIRouter()


@router.post('/notify', tags=['notification'])
async def ad_notification(phone: str, link: str, count: int):
    """
    A **POST** method that notify user about new ad for user's search request.
    """
    user = db.select_user(phone=phone)
    if not user:
        return {'Error': f'User with phone {phone} not found.'}
    user_id = user[0]
    message = (
        f'🧨Появилось новое объявление по твоему запросу.\n'
        f'Всего объявлений: {count}.\n'
        f'<a href="{link}">Проверить</a>'
    )
    await dp.bot.send_message(user_id, message)
    return {'status': 'OK'}


@router.post('/change_password', tags=['change_password'])
async def change_password(phone: str, link: str):
    """
    A **POST** method that send link for change password.
    """
    user = db.select_user(phone=phone)
    if not user:
        return {'Error': f'User with phone {phone} not found.'}
    user_id = user[0]
    message = (
        f'<a href="{link}">Сменить пароль</a>'
    )
    await dp.bot.send_message(user_id, message)
    return {'status': 'OK'}
