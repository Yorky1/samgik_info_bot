"""
Default echo bot
"""

import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import bot_data

bot = telebot.TeleBot(os.environ['SECRET_TOKEN'],parse_mode='HTML')

def keyboard(key_type="Normal"):
    """Keybourd for messages"""
    markup = ReplyKeyboardMarkup(row_width=1)
    if key_type == "Normal":
        for question in bot_data.questions_answers:
            markup.add(KeyboardButton(question))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Says hello."""
    bot.send_message(message.chat.id,bot_data.welcome_message,reply_markup=keyboard())

def correct_message(message):
    """Check message correctness."""
    return message.text in bot_data.questions_answers

@bot.message_handler(func=correct_message)
def answer_question(message):
    """Answer question."""
    bot.reply_to(message, bot_data.questions_answers[message.text])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Answer every incorrect message."""
    bot.reply_to(message, 'Ты задал вопрос, на который я не знаю ответа :(')

bot.infinity_polling()
