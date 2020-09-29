import telebot

from app import transactions, keyboards, settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    user = transactions.get_user(user_id=message.from_user.id)
    try:
        user or transactions.add_user(user_id=message.from_user.id)
    except transactions.UserNotAddedError:
        pass
    bot.send_message(message.chat.id, 'Menu:', reply_markup=keyboards.menu)


@bot.message_handler(func=lambda msg: msg.text == keyboards.SHOW_ALL)
def show_all_cards(message):
    bot.reply_to(message, )

