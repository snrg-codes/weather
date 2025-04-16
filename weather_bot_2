import telebot
from telebot import types
import requests

bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Location", request_location=True)
	markup.add(btn1)
	bot.send_message(message.chat.id, "Iltimos lokatsiyangizni jo'nating", reply_markup=markup)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    WEATHER_MAP_API_KEY = "OPENWEATHERMAP_API_KEY"
    lat = message.location.latitude
    lon = message.location.longitude
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_MAP_API_KEY}&units=metric"
    info = requests.get(url).json()
    city_name = info["name"]
    temp = info["main"]["temp"]
    bot.reply_to(message, f"{city_name} da harorat {temp} C ni ko'rsatmoqda")
bot.infinity_polling()
