from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
updater = Updater(token='6554753630:AAG2wV-XPV7mfuD7eMJTxnyEfxsXHLt6PpI', use_context=True)

def ban_user(update, context):
    user = update.message.left_chat_member
    
    # Replace 'YOUR_CHANNEL_ID' with the ID of your channel
    channel_id = -1001900546867
    
    if update.message.chat_id == int(channel_id):
        context.bot.kick_chat_member(chat_id=channel_id, user_id=user.id)

updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, ban_user))

updater.start_polling()
updater.idle()
