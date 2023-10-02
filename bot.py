import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from logging import basicConfig, getLogger, INFO

basicConfig(level=INFO)
log = getLogger()

# Define your bot token
TOKEN = '6535562523:AAFAw-u0ENKuMoe0sE7MT1RFwTLODQ35aso'

# Create an updater object
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the handler function for the /start command
def start(update, context):
    update.message.reply_text(
        "start this bot",
        parse_mode="markdown")

def help(update, context):
    update.message.reply_text(
        "help for this bot",
        parse_mode="markdown")

# Define the handler function for when a user leaves the channel
def left_channel(update, context):
    user_id = update.message.left_chat_member.id
    context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)

# Add handlers to the dispatcher
start_handler = MessageHandler(Filters.command & Filters.regex('^/start$'), start)
left_channel_handler = MessageHandler(Filters.status_update.left_chat_member, left_channel)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(left_channel_handler)

# Start the bot
updater.start_polling()
