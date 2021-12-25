"""
Default echo bot
"""

import os
import telebot

bot = telebot.TeleBot(os.environ['SECRET_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Says hello."""
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Echo every message."""
    bot.reply_to(message, "hi")

bot.infinity_polling()
