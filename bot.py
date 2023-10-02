import telebot

# Replace 'YOUR_TOKEN' with your actual Telegram Bot token
bot = telebot.TeleBot('5449793938:AAGlcRydVK08XQ9fBM0d4Pxzm0yEJR898Kg')

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    # Check if the new member is leaving the channel
    if message.left_chat_member:
        user_id = message.left_chat_member.id
        chat_id = message.chat.id
        
        # Ban the user from the channel
        bot.kick_chat_member(chat_id, user_id)
        
        # Send a message to notify about the ban
        bot.send_message(chat_id, f"User {user_id} has been banned.")
        
# Start the bot
bot.polling()
