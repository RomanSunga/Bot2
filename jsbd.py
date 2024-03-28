import requests
from bs4 import BeautifulSoup
import sqlite3

# Устанавливаем соединение с базой данных (или создаем новую, если ее нет)
conn = sqlite3.connect('links.db')

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()

# Создаем таблицу, если она еще не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS Links
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT,
                genre TEXT)''')

url = 'https://studioband.info/tops.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')

count = 0
for link in links:
    if count < 100:
        href = link.get('href')
        if href:  # Проверяем, что ссылка существует
            genre = link.text  # Предполагаем, что текст ссылки используется в качестве жанра
            if not genre.isdigit():  # Проверяем, что жанр не является числом (годом)
                # Добавляем ссылку и жанр в базу данных
                cursor.execute("INSERT INTO Links (link, genre) VALUES (?, ?)", (href, genre))
                count += 1
    else:
        break

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()












