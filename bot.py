import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the function to handle the /start command
def start(update: Update, context):
    update.message.reply_text('Hello! I am a join request accepter bot.')

# Define the function to handle new member join requests
def new_member(update: Update, context):
    # Get the user ID of the new member
    user_id = update.message.new_chat_members[0].id
    
    # Accept the join request by sending a message with the command /accept_join_request followed by the user ID
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'/accept_join_request {user_id}')

# Define the function to handle the /accept_join_request command
def accept_join_request(update: Update, context):
    # Get the user ID from the command arguments
    user_id = context.args[0]
    
    # Accept the join request by calling the bot's method to add a user to a chat
    context.bot.add_chat_member(chat_id=update.effective_chat.id,
                                user_id=user_id)
    
    update.message.reply_text(f'Join request from user {user_id} accepted!')

def main():
    # Create an instance of Updater and pass your bot token
    updater = Updater("5449793938:AAEbBiKgcwFDdF8bx3NRg1tES5TeOypsJLw", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for different commands and messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    dp.add_handler(CommandHandler("accept_join_request", accept_join_request))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()

if __name__ == '__main__':
    main()
