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

def correct_message(message):
    """Check message correctness."""
    return message.text.isdigit() and 1 <= int(message.text) <= 10

@bot.message_handler(func=correct_message)
def answer_question(message):
    """Answer question."""
    bot.reply_to(message, bot_data.questions[int(message.text) - 1])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Answer every incorrect message."""
    bot.reply_to(message, 'Введи номер от 1 до 10, чтобы я смог ответить на твой вопрос')

bot.infinity_polling()
