"""
Default echo bot
"""

import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import bot_data

bot = telebot.TeleBot(os.environ['SECRET_TOKEN'],parse_mode='HTML')

def keyboard(key_type="standart"):
    """Keyboard for messages"""
    markup = ReplyKeyboardMarkup(row_width=1)
    if key_type == "standart":
        for question in bot_data.questions_answers:
            markup.add(KeyboardButton(question))
    elif key_type == "faq":
        for question in bot_data.faq:
            markup.add(KeyboardButton(question))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Says hello."""
    bot.send_message(message.chat.id,bot_data.welcome_message,reply_markup=keyboard("standart"))

@bot.message_handler(func=lambda message: message.text == "Выйти")
def answer_question(message):
    """Exit message"""
    bot.send_message(message.chat.id,"Окей, переходим в главное меню",reply_markup=keyboard("standart"))

@bot.message_handler(func=lambda message: message.text in bot_data.faq)
def answer_faq(message):
    """Answer question."""
    bot.reply_to(message, bot_data.faq[message.text])
        
@bot.message_handler(func=lambda message: message.text in bot_data.questions_answers)
def answer_question(message):
    """Answer question."""
    if message.text == "Часто задаваемые вопросы":
        bot.send_message(message.chat.id,"Выбери вопрос из списка",
            reply_markup=keyboard("faq"))
    else:
        bot.reply_to(message, bot_data.questions_answers[message.text])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Answer every incorrect message."""
    bot.reply_to(message, "Ты задал вопрос, на который я не знаю ответа :( Выбери что-нибудь из меню")

bot.infinity_polling()
