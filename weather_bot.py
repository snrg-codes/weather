import telebot
import requests
from weather import get_weather
from typing import Dict, Optional
from datetime import datetime

WEATHER_API_KEY = "WEATHER_API"

bot = telebot.TeleBot("TELEGRAM_BOT_API")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        weather_data = get_weather(message.text, WEATHER_API_KEY)
        if weather_data:
            bot.reply_to(message, 
            f"Weather in {weather_data['city']}: {weather_data['temperature']}")
    except:
        text = "This city does not exist"
        bot.reply_to(message, text)

bot.infinity_polling()
