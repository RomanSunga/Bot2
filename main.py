import telebot
from telebot import types
import sqlite3
conn = sqlite3.connect('links.db')
cursor = conn.cursor()
import random



bot = telebot.TeleBot('7158364646:AAF5SJorIUaCPBU7t3v7sShKVl_KmsPF3hM')
@bot.message_handler(commands=['link'])
def send_random_link(message):
    cursor.execute("SELECT link FROM links")
    all_link = cursor.fetchall()

    if all_link:
        random_link = random.choice(all_link)[0]
        bot.send_message(message.chat.id, all_link)
    else:
        bot.send_message(message.chat.id, "Извините, но вы все пересмотрели.")
    
name = None
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Подборка аниме', url = 'https://shikimori.one/collections/3981-500-samyh-populyarnyh-anime-na-shikimori')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Подборка фильмов ', url = 'https://premier.one/collections/top-250-filmov-na-premier')
    btn3 = types.InlineKeyboardButton('Подборка ютуб каналов ', url = 'https://icanchoose.ru/blog/60-samyh-interesnyh-kanalov-na-youtube/')
    markup.row(btn2, btn3)
    file = open('./ocr.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name},  я БОТ который будет рекомендовать тебе аниме, в зависимости от твоих предпочтений.', reply_markup=markup)




bot.polling()
conn.close()










