from telethon.sync import TelegramClient, events
from telethon import Button
import random
import time

# Replace the values below with your own API credentials
api_id = 7630000
api_hash = 'f70361ddf4ec755395b4b6f1ab2d4fae'
bot_token = '5449793938:AAHfGttioxLqN2SnWHQevRFaljklaOo0WXg'
image_paths = ['image/img1.jpeg', 'image/img2.jpeg', 'image/img3.jpeg']

# Create a TelegramClient instance
client = TelegramClient('userbot_session', api_id, api_hash).start(bot_token=bot_token)

# Function to send a message to the channel owner
async def send_banned_user_message(channel_id, user_name):
    message = f"The user {user_name} has been banned from your channel."
    await client.send_message(channel_id, message)

@client.on(events.ChatAction)
async def handle_chat_action(event):
    if event.user_joined:
        print(f"User joined: {event.user_id}")
    elif event.user_left:
        print(f"User left: {event.user_id}")
        try:
            await client.edit_permissions(event.chat_id, event.user_id, view_messages=False)
            print(f"Banned user: {event.user_id}")
            # Get the channel ID from the event object
            channel_id = event.chat_id
            # Get the banned user's name from the event object (assuming it's available)
            user_name = event.user.first_name if event.user.first_name else "Unknown User"
            # Send a message to the channel owner with the banned user's name and channel name
            await send_banned_user_message(channel_id, user_name)
            time.sleep(4)
        except Exception as e:
            print(f"Failed to ban user: {e}")
            time.sleep(4)
            
# Create a new TelegramClient instance
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Path to the image file
    image_path = random.choice(image_paths)
    # Caption for the image
    caption = 'Ｈｅｙ, Ｗｅｌｃｏｍｅ \n\nɪ ᴄᴀɴ ʙᴀɴ ᴜꜱᴇʀꜱ ᴡʜᴏ ʟᴇᴀᴠᴇꜱ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪɴ ʟᴇꜱꜱ ᴛʜᴇɴ 1ꜱᴇᴄ \n\nʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ: /help'
    
    # Create the URL buttons
    button1 = Button.url('𝗟𝗲𝗴𝗲𝗻𝗱𝘅𝗧𝗿𝗶𝗰𝗸𝘀', 't.me/LegendxTricks')
    button2 = Button.url('𝗜𝗺𝗽𝗮𝗰𝘁 𝗪𝗼𝗿𝗹𝗱', 't.me/IMPACT_WORLD')
    
    # Send the message with the image and buttons
    await client.send_file(event.chat_id, file=image_path, caption=caption, buttons=[[button1, button2]])
    time.sleep(3)
                             ####

@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    # Path to the image file
    image_path = random.choice(image_paths)
    # Caption for the image
    caption2 = '𝗨𝘀𝗮𝗴𝗲 𝗶𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻𝘀.\n\nAᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴏʀ, ᴡɪᴛʜ "ʙᴀɴ ᴜꜱᴇʀ" ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴀɴᴅ ɪ ᴡɪʟʟ ɪɴꜱᴛᴀɴᴛʟʏ ꜱᴛᴀʀᴛ ᴍʏ ᴡᴏʀᴋ.'
    button3 = Button.url('𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', 'https://t.me/LxtBanBot?startchannel=xAaYux&admin=invite_users+manage_chat')
    
    # Send the message with the image and buttons
    await client.send_file(event.chat_id, file=image_path, caption=caption2, buttons=[button3])


    time.sleep(3)
# Start the event loop
client.run_until_disconnected()
