import telebot
from telebot import types

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = "6261425349:AAHDEepvXBWlmmL0cu-vSDr6_ZF86K1amyI"

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id, 'typing')

    # Create inline keyboard with a single button
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            "🤖 My Bots", callback_data="button_clicked"),
        types.InlineKeyboardButton("My Channle", url="https://t.me/GTIDev"))

    markup.add(
        types.InlineKeyboardButton("📢 Contact Me", callback_data="contact_home"))

    # Add user's clickable name to the message
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    bot.send_message(
        chat_id,
        f"Hi {mention}, \n\nthis bot lets you contact me and know more about me.",
        parse_mode='HTML',
        reply_markup=markup)


# Start the bot
print("Hey, I am up...")
bot.polling()
