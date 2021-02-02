from fastapi import APIRouter

router = APIRouter()


@router.post('/notify', tags=['notification'])
async def ad_notification(
    phone: str,
    link: str,
    count: int
):
    """
    A **POST** method that notify user about new ad for user's search request.
    """

    return {'status': 'OK'}
