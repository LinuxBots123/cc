from telethon.sync import TelegramClient, events

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '7630000'
api_hash = 'f70361ddf4ec755395b4b6f1ab2d4fae'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6535562523:AAHVrSvHKQq796SS6xFqbldkhhcXaCbE4OM'

# Replace 'YOUR_CHANNEL_USERNAME' with your actual channel username (e.g., @your_channel)
channel_username = 'LegendxTricks'

with TelegramClient('session_name', api_id, api_hash) as client:
    @client.on(events.ChatAction)
    async def handle_chat_action(event):
        if event.user_joined or event.user_left:
            user_id = event.user_id
            chat_id = await client.get_entity(channel_username)
            
            try:
                await client.kick_participant(chat_id, user_id)
                print(f"User {user_id} has been banned from the chat.")
            except Exception as e:
                print(f"Failed to ban user: {e}")
    
    client.run_until_disconnected()
