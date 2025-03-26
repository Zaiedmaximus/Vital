from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the token from the environment variable
TOKEN = os.getenv('T7589021047:AAEZNPnvIimVaCZzuj5ZpfYx9qPWVKckeXs')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when /start is issued."""
    await update.message.reply_text('Hello! I am your bot.')

def main():
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler('start', start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
