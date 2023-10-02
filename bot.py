import os
from telegram.ext import Updater, CommandHandler

# Get the Telegram bot token from environment variable
TOKEN = ('5449793938:AAEbBiKgcwFDdF8bx3NRg1tES5TeOypsJLw')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

def main():
    # Create an instance of the Updater class with your bot token
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=int('8443'), url_path=TOKEN)
    
    # Set the webhook URL for Heroku deployment
    updater.bot.setWebhook("https://ghikhhg.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
