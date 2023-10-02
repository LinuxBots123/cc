import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6535562523:AAGrUeW5atwGtbX6_rbUqL5c1NNRwYoW7KU')

@bot.channel_post_handler(content_types=['left_chat_member'])
def handle_left_chat_member(message):
    user_id = message.left_chat_member.id
    chat_id = message.chat.id
    
    # Replace 'YOUR_CHANNEL_ID' with your actual channel ID
    if chat_id == -1001900546867:  # Check if the user left from your channel
        bot.kick_chat_member(chat_id, user_id)  # Ban the user from the channel

# Start the bot
bot.polling()
