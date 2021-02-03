import uvicorn
from fastapi import FastAPI

from api_routers import notification


tags_metadata = [
    {
        "name": "notification",
        "description": "Notify user about new ad.",
    },
    {
        "name": "change_password",
        "description": "Send message with link for change password.",
    },
]
app = FastAPI(
    title="Spider API for CarsPass Telegram Bot",
    version="0.0.1",
    openapi_tags=tags_metadata,
)
app.include_router(notification.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
