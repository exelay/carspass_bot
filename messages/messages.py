msg_hello = (
    "Привет, {}! Для авторизации воспользуйся командой /auth. "
    "Если нужно подтвердить оплату /paid." 
    "Для получения уведомлений, включи их в разделе «избранный поиск»"
)
msg_help = (
    "Help message here\n"
    "/start - Start the bot\n"
    "/help - This help message"
)
msg_auth_success = "Авторизация прошла успешно.\nТвой код: <code>{}</code>"
msg_auth_fail = "Авторизация не удалась, мы не нашли пользователя с таким номером."

MESSAGES = {
    'hello': msg_hello,
    'help': msg_help,
    'auth_success': msg_auth_success,
    'auth_fail': msg_auth_fail,
}
