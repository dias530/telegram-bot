import telebot
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

API_URL = "https://api-inference.huggingface.co/models/AK391/animefy"
API_KEY = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_anime(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.content

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "⏳ Сурет өңделуде... 5-10 секунд күтіңіз.")
    
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded = bot.download_file(file_info.file_path)
    
    result = generate_anime(downloaded)

    bot.send_photo(message.chat.id, result, caption="✨ Аниме-стиль дайын!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Сәлем! Маған фото жіберсең, мен оны аниме стиліне айналдырамын 😎")

bot.polling()
