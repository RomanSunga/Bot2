import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from bs4 import BeautifulSoup
import app.keyboards as kb
import random

router = Router()





@router.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer_sticker('CAACAgIAAxkBAAEL8npmIW5tVf_A2HOIXh7e9dPVeSTYgwACVzIAAlZfGEuQ00oChUPYQzQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8nxmIW5xuuIVlSg1jbSReusrur94PQACKiUAAua_GUtodTWTfplsujQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8n5mIW5zwuVvP-4Gbt3dOCMmSJl4eAACuS8AAgS3EEuL1jlbFPjxTTQE')
   await message.answer(f'Привет,{message.from_user.first_name}, я бот который будет давать ссылку на аниме☢️',
                        reply_markup=kb.main)

@router.message(Command('Instructions'))
async def inst_message(message: Message):
    await message.answer("Если вы хотите получить аниме, нажмите кнопку ПОЛУЧИТЬ. Так же вы можете получать аниме по вашему вкусу нажми кнопку ЗАРЕГИСТРИРОВАТЬСЯ.")


# Парсинг ссылок с сайта
#def parse_links():
   #url = 'https://studioband.info/tops.html'
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #links = [a['href'] for a in soup.find_all('a', href=True)]
    #return links

# Запись ссылок в файл
#def write_to_file(links):
    #with open('links.txt', 'w') as file:
        #for link in links:
            #file.write(link + '\n')

# Обработчик команды /getlinks
#@router.message(Command('pars'))
#async def send_links(message: types.Message):
    #links = parse_links()
    #write_to_file(links)
    #await message.answer("Ссылки успешно добавлены в файл!")

# Обработчик команды /link
@router.message(F.text == 'Получить')
async def send_random_link(message: Message):
    with open('links.txt', 'r') as file:
        links = file.readlines()
        random_link = random.choice(links).strip()
        await message.answer(random_link)


@router.message(F.photo)
async def photo_message(message: Message):
    await message.reply("Следуй инструкции дебил🤡")

@router.message(F.text)
async def get_text(message: Message):
    await message.reply("Следуй инструкции дебил🤡")




