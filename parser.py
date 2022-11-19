import telebot
from telebot import types


Token = '5631725561:AAEEzzCjJl5vzVQ-NQEs9ShgpzhFzIB9tkg'
bot = telebot.TeleBot(Token)
total = 1000
taxiPrice = 150
foodPrice = 100
totalMinus = 0

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет , {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')
 

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    Домой = types.KeyboardButton('Такси')
    Помощь = types.KeyboardButton('Еда')
    Пополнить = types.KeyboardButton('Пополнить')
    markup.add(Домой, Помощь, Пополнить)
    bot.send_message(message.chat.id, ' Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['restart'])
def restart(message):
    global total
    total = 1000
    bot.send_message(message.chat.id, f'Вы обновили кошелек')

@bot.message_handler(content_types=['text'])
def game(message):
    global total
    global totalMinus
    if message.text =='Пополнить':
        total = 1000
        bot.send_message(message.chat.id, f'Вы пополнили кошелек до {total}')
    elif message.text == 'Такси':
        totalMinus = totalMinus + taxiPrice
        localTotal = total
        validate = localTotal - taxiPrice
        if validate > 0 and total > validate:
            total = total - taxiPrice
            bot.send_message(message.chat.id, f'Оплатили за такси {taxiPrice}. Осталось {total}')
        else:
            bot.send_message(message.chat.id, 'У вас недостаточно денег')
    elif message.text =='Еда':
        totalMinus = totalMinus + taxiPrice
        localTotal = total
        validate = localTotal - foodPrice
        if validate > 0 and total > validate:
            total = total - foodPrice
            bot.send_message(message.chat.id, f'Оплатили за еду {foodPrice}. Осталось {total}')
        else:
            bot.send_message(message.chat.id, 'У вас недостаточно денег')
    else:
        bot.send_message(message.chat.id, 'Я не понял, что вы хотите от меня')


bot.polling( )

