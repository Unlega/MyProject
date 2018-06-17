import telebot
import constants
from constants import token1
bot = telebot.TeleBot(constants.token1)

@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = '''Приветствую тебя друг!!!
    Ты находишься в Административной панели бота автопродаж.
    Вот список доступных команд:
    /des - добавит описание твоего магазина. То, что пользователь
    увидит, нажав кнопку '/start'.
    /help - инструкции под кнопку 'помощь'
    /gorod - После ее ввода добавляется новый город и автоматически
    продолжается ввод данных по предлагаемым тобой товарам.
    /set - Настройка существующего бота'''

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row("Добавить нового бота")
    user_markup.row("Настройка существующего")
   
    user_markup.row("В главное меню", "Прайс", "Помощь")
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['set'])
def handle_text(message):
      

if __name__ == '__main__':
    bot.polling(none_stop=True)
 
    
''' 
   log(message, answer)
    bot.send_message(message.chat.id,answer)
    
@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Тут пусто)"
    log(message, answer)
    bot.send_message(message.chat.id,answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты поц, гыгы"
    if message.text == "#":
        answer = str('b')
        log(message, answer)
        bot.send_message(message.chat.id, answer)

    elif message.text == "e":
        answer = "Ты лол"
        log(message, answer)
        bot.send_message(message.chat.id,answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id,answer)


@bot.message_handler(commands=['start'])
def begin(message):
    for id in users_id:
        if id != message.from_user.id:
            users_id.append(message.from_user.id)
            print(users_id) '''

