import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the referral dictionary to store referral codes and their corresponding users
referral_dict = {}

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    
    # Check if the user already has a referral code
    if user_id in referral_dict:
        referral_code = referral_dict[user_id]
        update.message.reply_text(f"You already have a referral code: {referral_code}")
    else:
        # Generate a new referral code for the user
        referral_code = generate_referral_code()
        referral_dict[user_id] = referral_code
        
        # Create the referral link with the generated code
        referral_link = f"https://t.me/your_bot_username?start={referral_code}"
        
        update.message.reply_text(f"Your referral code is: {referral_code}\n"
                                  f"Share this link with your friends to earn rewards: {referral_link}")

# Define the callback query handler for when someone starts using a referral code
def handle_referral(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    # Get the referred user's ID from the callback data
    referred_user_id = int(query.data)
    
    # Get the referrer's ID from the original message
    referrer_user_id = query.message.chat_id
    
    # Check if the referred user already has a referral code
    if referred_user_id in referral_dict:
        query.answer("You have already used a referral code.")
    else:
        # Add the referrer's ID as the referred user's referrer
        referral_dict[referred_user_id] = referrer_user_id
        
        query.answer("Referral code successfully used!")
        
        # Send a message to the referrer to notify them about the successful referral
        context.bot.send_message(chat_id=referrer_user_id, text="Congratulations! You have earned a referral reward.")

# Generate a random 6-digit alphanumeric referral code
def generate_referral_code() -> str:
    import random
    import string
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

def main() -> None:
    # Create the Updater and pass in your bot token
    updater = Updater("6554753630:AAFcrNNeTANaEp2SgB94sDmHy7meWww7pjk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the callback query handler for referrals
    dispatcher.add_handler(CallbackQueryHandler(handle_referral))

    # Start the Bot
    updater.start_polling()

if __name__ == '__main__':
    main()
