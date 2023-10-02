from telegram import Update
from telegram.ext import Updater, CommandHandler, ChatMemberHandler, CallbackContext
from telegram.constants import CHAT_MEMBER_LEFT

# Define your bot token here
TOKEN = "6535562523:AAHVrSvHKQq796SS6xFqbldkhhcXaCbE4OM"
# Define your channel ID here
CHANNEL_ID = -1001900546867

def ban_user(update: Update, context: CallbackContext):
    """Handler for the chat member updates"""
    chat_member_update = update.chat_member
    if chat_member_update.status == CHAT_MEMBER_LEFT:
        user_id = chat_member_update.from_user.id
        context.bot.kick_chat_member(CHANNEL_ID, user_id)

def main():
    # Create an instance of the Updater class with your bot token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the ban_user handler for chat member updates
    dispatcher.add_handler(ChatMemberHandler(ban_user))

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()
