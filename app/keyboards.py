import telebot

SHOW_ALL = 'Show all'
CREATE_CARD = 'Create card'
DELETE_CARD = 'Delete card'
EDIT_CARD = 'Edit card'
SEARCH = 'Search'


menu = telebot.types.ReplyKeyboardMarkup()
menu.add(telebot.types.KeyboardButton(SHOW_ALL))
menu.add(telebot.types.KeyboardButton(CREATE_CARD))
menu.add(telebot.types.KeyboardButton(DELETE_CARD))
menu.add(telebot.types.KeyboardButton(EDIT_CARD))
menu.add(telebot.types.KeyboardButton(SEARCH))
