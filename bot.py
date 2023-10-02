from telethon.sync import TelegramClient, events

# Replace the values below with your own API credentials
api_id = 7630000
api_hash = 'f70361ddf4ec755395b4b6f1ab2d4fae'
bot_token = '6535562523:AAGGQ0ivPpUbDrFuGlJiJ5lN-qZNt6hyhDM'

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

#################

@client.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    # Create a button for running the membership checker
    button = Button.inline('Check Membership', data='membership_check')
    
    # Send a welcome message with the button when the /start command is used
    await event.respond('🙋‍♂ Hello,\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔎 You Have To Join Our Channels By Below Buttons In Order To Use Me !!! After Joined! Press On Joined To Continue.\n➖➖➖➖➖➖➖➖➖➖➖➖➖', buttons=button)

@client.on(events.CallbackQuery)
async def handle_button_click(event):
    if event.data == b'membership_check':
        # Check if the user is a member of a specific channel or chat
        chat_username = 'LegendxTricks'
        user_id = event.sender_id
        
        try:
            # Get information about the user's membership in the chat
            participant = await client.get_participant(chat_username, user_id)
            
            if participant:
                await event.answer('You have joined the chat!')
                
                # Send a message with an inline link to another website
                link_button = Button.url('Ｕｐｄａｔｅｓ ', 't.me/LegendxTricks')
                await event.respond('Click on this link:', buttons=link_button)
                
            else:
                await event.answer('You have not joined the chat.')
        
        except Exception as e:
            print(e)
            await event.answer('An error occurred while checking your membership.')
            
# Start the event loop
client.run_until_disconnected()
