import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('5449793938:AAFKJYpDRiH18NYeU183SDDUHPWuhSR9dp0')

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    # Get the list of new chat members
    new_members = message.new_chat_members
    
    # Iterate through each new member and accept their join request
    for member in new_members:
        try:
            bot.restrict_chat_member(message.chat.id, member.id, can_send_messages=True)
            print(f"Accepted join request for user: {member.username}")
        except Exception as e:
            print(f"Failed to accept join request for user: {member.username}. Error: {e}")

# Start the bot
bot.polling()
