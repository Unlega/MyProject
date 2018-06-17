# -*- coding: utf-8 -*-
import json

'''
import requests
api_access_token = '' # токен можно получить здесь https://qiwi.com/apipip
my_login = '' # номер QIWI Кошелька в формате +79991112233

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + api_access_token
parameters = {'rows': '10'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+my_login+'/payments', params = parameters)
print(json.loads(h.text))'''

import telebot
import constants
from constants import txt1, txt2, txt3, txt4, txt5k, txt6k, txt5a, txt6a, txt7_a03, txt7_a05, txt7_k03,\
                        txt7_k05, txt8_k03g, txt8_k05g, txt8_a05g, txt8_k05g, txt9, Kbat03, Kbat05, Kbat10, Kkt03, Kkt05, Kkt1,\
                        Abat03, Abat05
#Alm[*], uvse[*]
from datetime import datetime
from users import botusers
bot = telebot.TeleBot(constants.token)
file = globals
@bot.message_handler(commands=['start'])
def handle_start(message):
    #Запишем в users нового пользователя
    
    if message.from_user.id not in botusers:
        botusers.append(message.from_user.id)
        print('!!!!!!!!!!!!++++++++++++++!!!!!!!!!!!')
        with open('users.py','w') as file:
            file.write('botusers='+str(botusers))

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row("Караганда", "!!!!Алмата")
    user_markup.row("Контакты магазина", "Ненаход")
    user_markup.row("Инструкция по оставлению отзыва в боте")
    user_markup.row("В главное меню", "Прайс", "Помощь")
    bot.send_message(message.from_user.id, txt1, reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global answer
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    # Общие клавиши
    if message.text == "В главное меню":
        answer = txt1
        user_markup.row("Караганда", "Алмата")

    if message.text == "Контакты магазина":
        answer = txt2
        user_markup.row("Караганда", "Алмата")

    if message.text == "Ненаход":
        answer = txt3
        user_markup.row("Караганда", "Алмата")

    if message.text == "Прайс":
        answer = txt4

    # Караганда
    if message.text == "Караганда":
        answer = txt5k
        user_markup.row("Батарея Energizer")

    if message.text == "Батарея Energizer":
        answer = txt6k
        user_markup.row(Kbat03, Kbat05)

    if message.text == Kbat05:
        answer = txt7_k05
        user_markup.row("Город")

    if message.text == Kbat03:
        answer = txt7_k03
        user_markup.row("Город")

    if message.text == "Город":
        answer = txt8_k03g
        user_markup.row("Qiwi")

    if message.text == "Qiwi":
        answer = txt9
        user_markup.row("Проверить оплату")

    # Алмата
    if message.text == "Алмата":
        answer = txt5a
        user_markup.row("Батарея Energizer.")

    if message.text == "Батарея Energizer.":
        answer = txt6a
        user_markup.row(Abat03, Abat05)

    if message.text == Abat05:
        answer = txt7_a05
        user_markup.row("Город")

    if message.text == Abat03:
        answer = txt7_a03
        user_markup.row("Город")

    if message.text == "Город":
        answer = txt8_a05g
        user_markup.row("Qiwi")

    if message.text == "Qiwi":
        answer = txt9
        user_markup.row("Проверить оплату")


    if answer is None:
        answer = "Неправильный выбор"

    user_markup.row("Контакты магазина", "Ненаход")
    user_markup.row("Инструкция по оставлению отзыва в боте")
    user_markup.row("В главное меню", "Прайс", "Помощь")

    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

    print("--------------------------------------------------------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}, message_id={4}) = {3}".format(
        message.from_user.first_name, message.from_user.last_name,
        str(message.from_user.id), message.text, message.message_id))
    print (botusers)
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0, timeout=500)


# Запишем в файл нового пользователя
'''if message.from_user.id not in users:
    users.append(message.from_user.id)

    with open('users.txt','w') as file:
        file.write('users.txt')
        print('users=', users)
        print('\n name=', message.from_user.first_name)
    file.close()

print("Сообщение от {0} {1}. (id = {2}) \n {3}",
        str(message.from_user.id, message.text)


    if message.text == "Ненаход":
        bot.send_message(message.from_user.id, 'Рой братан, отвечаю там лежит')
    else: bot.send_message(message.from_user.id, 'кнопки дави')'''
