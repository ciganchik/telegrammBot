TOKEN = '5192184670:AAEH91xmalc8Qo821sUFQEckffC66aFXQLg'

import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)
#  РАБОТА С КОМАНДАМИ /START
@bot.message_handler(commands= ['start'])
def welcome(message):
    mess = f'Приветсвую, {message.from_user.first_name}! \nЯ - <b></b>, бот созданный Артуром!'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# КНОПКИ 1
@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти", url="https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA+%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C+%D0%B8%D0%BC%D1%8F+%D0%B1%D0%BE%D1%82%D0%B0+%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%D0%BC+%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD&lr=106344"))
    bot.send_message(message.chat.id, "Открыть ссылку", reply_markup=markup)

# ОТСЛЕЖИВАНИЕ СООБЩЕНИЙ
@bot.message_handler(content_types= ['text'])
def first(message):
    if message.text == "Привет" or message.text == "привет":
     bot.send_message(message.chat.id, "Здравствуйте")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}", parse_mode='html')
    # ОТПРАВКА ФОТО
    elif message.text == "photo":
        photo = open('photo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == "сайт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        website = types.KeyboardButton('First')
        second = types.KeyboardButton('second')
        markup.add(website, second)
        bot.send_message(message.chat.id, "Выберети одну кнопку", reply_markup=markup)

    elif message.text == "First":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти", url="https://tonais.ru/osnovy/operatory-and-or-not-python"))
        bot.send_message(message.chat.id, "Открыть ссылку", reply_markup=markup)
    elif message.text == "second":
        photo = open('photo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, повоторите пожалуйста!")

# РАБОТА С ДОКУМЕНТАМИ
# ПРИНЯТИЕ ФОТО
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'hey bro, nice cock!')



# КНОПКИ 2
# @bot.message_handler(content_types=['text'])
# def website(message):

bot.polling(none_stop=True)