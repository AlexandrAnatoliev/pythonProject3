# pythonProject3

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
# По нажатию кнопки бот присылает случайный анекдот в личку

import telebot
import random
from telebot import types
import time
from config import token, channel

# Загружаем список анекдотов из файла
# если текстовый файл находится не в каталоге программы, то пишем полный путь к нему
# "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
f = open('fun.txt', 'r', encoding='UTF-8')
funs = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Анекдот")
    markup.add(item1)
    bot.send_message(m.chat.id,
                     'Нажми: \nАнекдот для получения интересного анекдота ',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный анекдот
    if message.text.strip() == 'Анекдот':
        answer = random.choice(funs)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


fl = 'start'
# посылаются случайные шутки через случайные периоды времени
while fl == 'start':
    bot.send_message(CHANNEL_NAME, random.choice(funs))
    time.sleep(random.randint(60, 3600))

# Запускаем бота
bot.polling(none_stop=True, interval=0)
