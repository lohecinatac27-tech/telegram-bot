from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace this with your actual bot token from BotFather
BOT_TOKEN = "6463586992:AAGFsjXN5zFLMaIDs7IskkUkGUuq9Cmh6OU"

# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

def main():
    # Create the bot application
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handler for /start
    app.add_handler(CommandHandler("start", start))

    # Run the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
