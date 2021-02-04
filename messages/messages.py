msg_hello = (
    "Привет, {}! Чтобы получать уведомления о новых автомобилях, "
    "нажми на кнопку ниже."
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
