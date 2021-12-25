"""
Default echo bot
"""

import os
import telebot

bot = telebot.TeleBot(os.environ['SECRET_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Says hello."""
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Echo every message."""
    bot.reply_to(message, questions[int(message.text)])

bot.infinity_polling()
