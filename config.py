import telebot
from pathlib import Path

key = "sk-KVD8VYoze5Ivy8BFwfV9KnCzdMvhnnyp"

DB_NAME = 'database.db'
current_path = Path.cwd()
theory_files_dir = current_path / 'datafiles' / 'theory_files'

token = '7917014135:AAFJealgiCNfbh6qotamVE4hLVkm7l-YmvI'
# Объект для взаимодействия с TelegramAPI
bot = telebot.TeleBot(token)