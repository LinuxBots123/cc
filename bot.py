from telethon.sync import TelegramClient, events
from telethon import Button
import random
# Replace the values below with your own API credentials
api_id = 7630000
api_hash = 'f70361ddf4ec755395b4b6f1ab2d4fae'
bot_token = '5643920525:AAEk92b0py5yTVqqU6x8yFcGZWXRH-zXxhQ'
image_paths = ['image/img1.jpeg', 'image/img2.jpeg', 'image/img3.jpeg']

# Create a TelegramClient instance
client = TelegramClient('userbot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.ChatAction)
async def handle_chat_action(event):
    if event.user_joined:
        print(f"User joined: {event.user_id}")
    elif event.user_left:
        print(f"User left: {event.user_id}")
        try:
            await client.edit_permissions(event.chat_id, event.user_id, view_messages=False)
            print(f"Banned user: {event.user_id}")
        except Exception as e:
            print(f"Failed to ban user: {e}")

# Create a new TelegramClient instance
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Path to the image file
    image_path = random.choice(image_paths)
    # Caption for the image
    caption = 'Ｈｅｙ, Ｗｅｌｃｏｍｅ \n\nɪ ᴄᴀɴ ʙᴀɴ ᴜꜱᴇʀꜱ ᴡʜᴏ ʟᴇᴀᴠᴇꜱ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪɴ ʟᴇꜱꜱ 1ꜱᴇᴄ \n\nʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ: /help'
    
    # Create the URL buttons
    button1 = Button.url('𝗟𝗲𝗴𝗲𝗻𝗱𝘅𝗧𝗿𝗶𝗰𝗸𝘀', 't.me/LegendxTricks')
    button2 = Button.url('𝗜𝗺𝗽𝗮𝗰𝘁 𝗪𝗼𝗿𝗹𝗱', 't.me/IMPACT_WORLD')
    
    # Create the message with the image and buttons
    message = await event.respond(file=image_path, caption=caption, buttons=[[button1, button2]])


# Start the event loop
client.run_until_disconnected()
