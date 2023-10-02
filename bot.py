from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5449793938:AAHM0rf-LCD-FU2VZ-aNEtpq4wgCQPLrUDA'

def handle_leave(update, context):
    user_id = update.message.left_chat_member.id
    chat_id = update.message.chat.id
    
    # Replace 'YOUR_CHANNEL_ID' with your actual channel ID
    channel_id = 'YOUR_CHANNEL_ID'
    
    if chat_id == channel_id:
        context.bot.kick_chat_member(chat_id, user_id)

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, handle_leave))
    
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
