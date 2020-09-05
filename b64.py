#telegram imports
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram.utils.helpers import escape_markdown
from uuid import uuid4

#encode decode imports
import configparser as cfg
import base64

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    user = update.message.from_user
    update.message.reply_text(
        'Hi ' + user['first_name'] + '!\n'
        'I\'m an encoding/decoding bot\n'
        'use /help for the help menu.')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        '====== Help Menu ======\n'
        'use /b64encode <text_to_encode> to encode into base 64 format\n'
        'use /b64decode <text_to_decode> to decode into base 64 format\n'
        'use /b32encode <text_to_encode> to encode into base 32 format\n'
        'use /b32decode <text_to_decode> to decode into base 32 format\n'
        'use /b16encode <text_to_encode> to encode into base 16 format\n'
        'use /b16decode <text_to_decode> to decode into base 16 format\n'
        )

def b64encode_text(update, context):
    user_reply = update.message.text
    encoded_text = base64.urlsafe_b64encode(str.encode(user_reply.replace('/b64encode ','').strip()))
    update.message.reply_text(encoded_text.decode("utf-8"))

def b64decode_text(update, context):
    user_reply = update.message.text
    formatted_reply = user_reply.replace('/b64decode ','').strip()
    decoded_text = base64.urlsafe_b64decode(formatted_reply)
    update.message.reply_text(decoded_text.decode("utf-8"))

def b32encode_text(update, context):
    user_reply = update.message.text
    encoded_text = base64.b32encode(str.encode(user_reply.replace('/b32encode ','').strip()))
    update.message.reply_text(encoded_text.decode("utf-8"))

def b32decode_text(update, context):
    user_reply = update.message.text
    formatted_reply = user_reply.replace('/b32decode ','').strip()
    decoded_text = base64.b32decode(formatted_reply)
    update.message.reply_text(decoded_text.decode("utf-8"))

def b16encode_text(update, context):
    user_reply = update.message.text
    encoded_text = base64.b16encode(str.encode(user_reply.replace('/b16encode ','').strip()))
    update.message.reply_text(encoded_text.decode("utf-8"))

def b16decode_text(update, context):
    user_reply = update.message.text
    formatted_reply = user_reply.replace('/b16decode ','').strip()
    decoded_text = base64.b16decode(formatted_reply)
    update.message.reply_text(decoded_text.decode("utf-8"))


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater('1387796289:AAFi8UJtUYFLhup1ADdrB5EK_w9aVuBLjBY', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("b64encode", b64encode_text))
    dp.add_handler(CommandHandler("b64decode", b64decode_text))
    dp.add_handler(CommandHandler("b32encode", b32encode_text))
    dp.add_handler(CommandHandler("b32decode", b32decode_text))
    dp.add_handler(CommandHandler("b16encode", b16encode_text))
    dp.add_handler(CommandHandler("b16decode", b16decode_text))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()