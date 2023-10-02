import requests
import time
import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('5449793938:AAEbBiKgcwFDdF8bx3NRg1tES5TeOypsJLw')

# Replace 'YOUR_CHANNEL_USERNAME' with your actual channel username (e.g., @mychannel)
channel_username = 'LegendxTricks'

# Replace 'YOUR_CHAT_ID' with the chat ID where you want to send the new post link
chat_id = '5488677608'

# Function to get the link of the latest post from your channel
def get_latest_post_link():
    url = f'https://api.telegram.org/bot{bot.token}/getChat'
    params = {'chat_id': channel_username}
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['ok']:
        latest_post_id = data['result']['last_message']['message_id']
        return f'https://t.me/{channel_username}/{latest_post_id}'
    
    return None

# Function to send the latest post link to the specified chat ID
def send_latest_post_link():
    latest_post_link = get_latest_post_link()
    
    if latest_post_link:
        bot.send_message(chat_id, latest_post_link)

# Main loop to check for new posts every 10 seconds and send them if available
while True:
    send_latest_post_link()
    time.sleep(10)
