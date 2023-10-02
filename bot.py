import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

    # Create the Updater and pass in your bot toke
updater = Updater("6554753630:AAFykeOjMMiCfCgv8AVPBuXHAm8swEdSVMM")
dispatcher = updater.dispatcher

# Define the start command handler
# Define the handler function for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

# Define the handler function for when a user leaves the channel
def left_channel(update, context):
    user_id = update.message.left_chat_member.id
    context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)

# Add handlers to the dispatcher
start_handler = MessageHandler(Filters.command & Filters.regex('^/start$'), start)
left_channel_handler = MessageHandler(Filters.status_update.left_chat_member, left_channel)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(left_channel_handler)

def main() -> None:
    # Start the Bot
    updater.start_polling()

if __name__ == '__main__':
    main()
