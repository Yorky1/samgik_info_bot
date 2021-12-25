"""
Default echo bot
"""

import os
import telebot
import bot_data

bot = telebot.TeleBot(os.environ['SECRET_TOKEN'],parse_mode='HTML')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Says hello."""
    bot.reply_to(message, bot_data.welcome_message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Echo every message."""
    bot.reply_to(message, bot_data.questions[int(message.text) - 1])

bot.infinity_polling()
