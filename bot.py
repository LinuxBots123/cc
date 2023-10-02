from telethon.sync import TelegramClient, events
from telethon.tl.custom import Button

api_id = 7630000
api_hash = 'f70361ddf4ec755395b4b6f1ab2d4fae'
bot_token = '6535562523:AAEnlx6PqANooLIEt2wp3yLVi9yhNCoIDCo'

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

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [[Button.inline("Help", b'help')]]
    await event.respond('Welcome to my bot!', buttons=buttons)

# Register an event handler for the /help command
@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    # Create an inline keyboard with a "Back" button
    buttons = [[Button.inline("Back", b'back')]]
    # Send a help message to the user with the inline keyboard
    await event.respond('This is a help message. Click "Back" to go back to start.', buttons=buttons)

# Register an event handler for handling button clicks
@client.on(events.CallbackQuery)
async def handle_button_click(event):
    if event.data == b'help':
        # Send a new message with the help text and back button
        buttons = [[Button.inline("Back", b'back')]]
        await client.send_message(event.chat_id, 'This is a help message. Click "Back" to go back to start.', buttons=buttons)
    elif event.data == b'back':
        # Execute the /start command when the "Back" button is clicked
        await start(event)




client.run_until_disconnected()
