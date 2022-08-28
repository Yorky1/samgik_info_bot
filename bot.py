#!/usr/bin/env python

# pylint: disable=unused-argument

"""

Bot

"""

import os
import logging

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, TypeHandler

from strings import (
    FINAL_REPLIES,
    STATE_MESSAGES,
    MENU_STATES,
    NEXT_STATE,
    REPLY_MARKUPS,
    STRING_STATES,
    ERROR_MESSAGE,
    SAMARA,
    MENU_STATE,
    START_FORM_STATE,
    CITY_STATE,
    GET_INSTITUTE_STATE,
    STATE,
    FACULTY,
    CITY,
    QUIZ_STATE,
    RIGHT_ANSWER,
    FREE_ANSWER,
    FACULTY_MESSAGES,
    FACULTIES,
    PREV_STATE,
    SET_FACULTY_STATE,
    CHAT_IDS,
    FINAL_STATE
)

DEBUG_MODE=False

# Enable logging

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

logger = logging.getLogger(__name__)

async def default_reply_by_state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Default reply message"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state],reply_markup=REPLY_MARKUPS[cur_state])

async def set_faculty_first(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Set the faculty for the first time"""
    context.user_data[FACULTY] = update.message.text
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    reply_text=FACULTY_MESSAGES[update.message.text]
    await context.bot.send_message(chat_id=chat_id, text=reply_text,reply_markup=REPLY_MARKUPS[cur_state])

async def view_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """View main menu"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    text = STATE_MESSAGES[cur_state].copy()
    text[1] += "<b>" + context.user_data.setdefault(FACULTY, FACULTIES[0]) + "</b>."
    await context.bot.send_message(chat_id=chat_id, text="\n".join(text),reply_markup=REPLY_MARKUPS[cur_state], parse_mode='HTML')

async def end_introduction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """End of introduction part"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state])
    context.user_data[STATE] = NEXT_STATE[cur_state]
    await view_menu(update, context)


async def final_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send final message"""
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[FINAL_STATE][1], parse_mode='HTML')
    await context.bot.send_sticker(chat_id=chat_id, sticker="CAACAgIAAxkBAAIMT2MIw7rMWBISWOcTJ-v3NvGL4Z0DAAIVIgACnhE5SKMY7CIGSdVXKQQ")
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def form(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Анкета' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    if cur_state == START_FORM_STATE:
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state])
        return

    if cur_state == CITY_STATE:
        city = update.message.text.lower()
        context.user_data[CITY] = city
        if city == SAMARA:
            await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][0],reply_markup=REPLY_MARKUPS[cur_state][0])
        else:
            await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][1],reply_markup=REPLY_MARKUPS[cur_state][1])
        return

    if cur_state == GET_INSTITUTE_STATE:
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state],reply_markup=REPLY_MARKUPS[cur_state])
        return

    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state])
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def knowledge_day(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'День знаний' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    for message in STATE_MESSAGES[cur_state]:
        await context.bot.send_message(chat_id=chat_id, text=message)
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def chants(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Кричалки' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    faculty = context.user_data.setdefault(FACULTY, FACULTIES[0])
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][faculty])
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def procession(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Шествие' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    faculty = context.user_data.setdefault(FACULTY, FACULTIES[0])
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][0])
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][1][faculty])
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def concert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Праздничный концерт' button"""
    chat_id = update.effective_chat.id
    with open("pics/concert.jpg", 'rb') as file_handler:
        await context.bot.send_photo(chat_id=chat_id, photo=file_handler)
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Контакты' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    faculty = context.user_data.setdefault(FACULTY, FACULTIES[0])
    await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][faculty], parse_mode='MarkdownV2')
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def about_sgik(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """'Про СГИК' button"""
    chat_id = update.effective_chat.id
    cur_state = context.user_data[STATE]
    if cur_state == QUIZ_STATE:
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state],reply_markup=REPLY_MARKUPS[cur_state])
        return

    message = update.message.text
    if message == RIGHT_ANSWER:
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][0][0])
    else:
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][0][1])

    for message_id in range(1, len(STATE_MESSAGES[cur_state])):
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[cur_state][message_id])

    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)

async def set_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Menu command"""

    cur_state = context.user_data[STATE]
    chat_id = update.effective_chat.id
    if cur_state != SET_FACULTY_STATE:
        context.user_data[PREV_STATE] = cur_state
        context.user_data[STATE] = SET_FACULTY_STATE
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[SET_FACULTY_STATE], reply_markup=REPLY_MARKUPS[SET_FACULTY_STATE])
        return

    context.user_data[FACULTY] = update.message.text
    context.user_data[STATE] = context.user_data[PREV_STATE]
    await MESSAGE_FUNCTION[context.user_data[STATE]](update, context)

MESSAGE_FUNCTION={
    1:default_reply_by_state,
    2:default_reply_by_state,
    3:set_faculty_first,
    4:end_introduction,
    5:view_menu,
    6:form,
    13:form,
    14:form,
    15:form,
    7:knowledge_day,
    8:chants,
    9:procession,
    10:concert,
    11:contacts,
    12:about_sgik,
    16:about_sgik,
    17:set_faculty,
    18:final_message
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start message"""
    context.user_data[STATE] = 1
    context.bot_data[CHAT_IDS].add(update.effective_chat.id)
    if DEBUG_MODE:
        print("CHAT_IDS=", context.bot_data[CHAT_IDS])
    await default_reply_by_state(update, context)

#TL;DR
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help message"""

    await update.message.reply_text("Help!")

def next_state(message: str, state: int) -> int:
    """Get next state."""
    result = 0
    if state == MENU_STATE:
        for message_id, menu_message in enumerate(MENU_STATES):
            if message == menu_message:
                result = NEXT_STATE[MENU_STATE][message_id]
    else:
        result = NEXT_STATE[state]
    return result

async def receive_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Message processing"""
    if STATE not in context.user_data:
        return

    message = update.message.text

    if message in FINAL_REPLIES:
        await final_message(update, context)
        return

    if context.user_data[STATE] in FREE_ANSWER and \
        (message not in STRING_STATES or context.user_data[STATE] != STRING_STATES[message]):
        return

    old_state = context.user_data[STATE]
    try:
        context.user_data[STATE] = next_state(message, context.user_data[STATE])
    except KeyError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ERROR_MESSAGE)
        return
    cur_state=context.user_data[STATE]
    if DEBUG_MODE:
        print("message= "+message+"\nold_state="+str(old_state)+"\nnext_state="+str(cur_state)+"\n")

    try:
        await MESSAGE_FUNCTION[cur_state](update, context)
    except KeyError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ERROR_MESSAGE)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Menu command"""
    context.user_data[STATE] = MENU_STATE
    await view_menu(update, context)


async def get_cur_state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get current state."""
    await context.bot.send_message(chat_id=update.effective_chat.id,text=str(context.user_data.setdefault(STATE, "No state")))

async def set_state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Set current state."""
    context.user_data[STATE]=int(context.args[0])
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Your current state is "+str(context.user_data[STATE]))

async def get_user_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gets information about all users"""

    await update.message.reply_text(str(context.bot_data))

async def sticker_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle non text objects"""
    print(update.message)

async def send_final_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send final message command"""
    for chat_id in context.bot_data[CHAT_IDS]:
        if DEBUG_MODE:
            print("Sending to", chat_id)
        await context.bot.send_message(chat_id=chat_id, text=STATE_MESSAGES[FINAL_STATE][0], reply_markup=REPLY_MARKUPS[FINAL_STATE])

async def send_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send gif command"""
    for chat_id in context.bot_data[CHAT_IDS]:
        if DEBUG_MODE:
            print("Sending to", chat_id)
        with open("pics/gifka.gif", 'rb') as file_handler:
            await context.bot.send_animation(chat_id=chat_id, animation=file_handler)

def main() -> None:

    """Start the bot."""

    application = Application.builder().token(os.environ['SECRET_TOKEN']).read_timeout(60).pool_timeout(60).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_text))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("set_faculty", set_faculty))
    application.add_handler(CommandHandler("send_final_message", send_final_message))
    application.add_handler(CommandHandler("send_gif", send_gif))
    if DEBUG_MODE:
        application.add_handler(CommandHandler("state", get_cur_state))
        application.add_handler(CommandHandler("set_state", set_state))
        application.add_handler(TypeHandler(type=object,callback=sticker_handler))

    application.bot_data[CHAT_IDS] = set()
    application.run_polling()

if __name__ == "__main__":
    main()
