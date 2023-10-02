from telegram.ext import Updater, MessageHandler, Filters

chat_id = "5488677608"

def handle_new_post(update, context):
    channel_username = "LegendxTricks"
    post_id = update.channel_post.message_id
    post_url = f"https://t.me/{channel_username}/{post_id}"
    
    message = f"New post: {post_url}"
    context.bot.send_message(chat_id=chat_id, text=message)

# Replace with your bot token
bot_token = "5449793938:AAFbYnwEHZyx_8JiWjxfUsXBGOursJIMbso"

updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Register the handler for new channel posts
dispatcher.add_handler(MessageHandler(Filters.Channel & Filters.update.channel_posts, handle_new_post))
# Start polling for updates
updater.start_polling()
