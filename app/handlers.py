import telebot

from app import transactions, settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not (user := transactions.get_user(user_id=message.from_user.id)):
        try:
            transactions.add_user(user_id=message.from_user.id)
        except transactions.UserNotAddedError:
            pass
    response = 'Welcome' if not user else 'Welcome again'
    bot.reply_to(message, response)
