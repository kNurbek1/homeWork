import telebot
from telebot import types

total = 1000
Token = '5631725561:AAEEzzCjJl5vzVQ-NQEs9ShgpzhFzIB9tkg'
bot = telebot.TeleBot(Token)
taxiPrice = 150
foodPrice = 100

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет , {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['site'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Такси', url= 'https://web.telegram.org/z/#5631725561'))
    markup.add(types.InlineKeyboardButton('Еда', url= 'https://web.telegram.org/z/#5631725561'))
        
@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    Домой = types.KeyboardButton('Домой')
    Помощь = types.KeyboardButton('Помощь')
    markup.add(Домой, Помощь)
    bot.send_message(message.chat.id, ' Перейдите на сайт', reply_markup=markup)

bot.polling()

