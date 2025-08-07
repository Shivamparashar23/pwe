#!/usr/bin/env python3

import re
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update

# Telegram bot token (replace with your BotFather token)
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Regular expression to match yt-dlp download commands
pattern = r'yt-dlp --no-warnings --progress --console-title -o "([^"]+)" "([^"]+)"'

async def start(update: Update, context):
    await update.message.reply_text("Send me a .sh file, and I'll extract the yt-dlp links into a .txt file in 'name:url' format!")

async def handle_file(update: Update, context):
    file = update.message.document
    if not file.file_name.endswith('.sh'):
        await update.message.reply_text("Please send a .sh file!")
        return

    # Download the file
    file_path = file.file_name
    new_file = await context.bot.get_file(file.file_id)
    await new_file.download_to_drive(file_path)

    # Read the input script
    try:
        with open(file_path, 'r') as f:
            script_content = f.read()
    except Exception as e:
        await update.message.reply_text(f"Error reading file: {str(e)}")
        os.remove(file_path)
        return

    # Find all matches
    matches = re.findall(pattern, script_content)
    if not matches:
        await update.message.reply_text("No yt-dlp links found in the file!")
        os.remove(file_path)
        return

    # Create output .txt file
    output_file = file_path.rsplit('.', 1)[0] + '.txt'
    try:
        with open(output_file, 'w') as f:
            for name, url in matches:
                f.write(f"{name}:{url}\n")
    except Exception as e:
        await update.message.reply_text(f"Error creating output file: {str(e)}")
        os.remove(file_path)
        return

    # Send the output file back to the user
    try:
        with open(output_file, 'rb') as f:
            await update.message.reply_document(document=f, filename=output_file)
        await update.message.reply_text(f"Download list created: {output_file}")
    except Exception as e:
        await update.message.reply_text(f"Error sending file: {str(e)}")
    finally:
        # Clean up files
        os.remove(file_path)
        os.remove(output_file)

def main():
    # Create the Application instance
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
