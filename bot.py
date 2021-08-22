import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Здравствуйте, я чат-бот проекта "Поехали".\nДля регистрации в проекте отпрвьте мне в чат свой логин в Инстаграмме.')

def help(update, context):
    update.message.reply_text('Currently I am in Alpha stage, help me also!')

def piracy(update, context):
    update.message.reply_text('Ahhan, FBI wants to know your location!')

def echo(update, context):
    if update.message.text == "Да":
        update.message.reply_text('Спасибо за регистрацию в проекте!\nПодробную информацию вы можете получить у нас в боте.\nУзнать список команд - /help')
    else:
        update.message.reply_text('Чтобы подтвердить участие в Маршруте отпрвьте "Да" ко мне в чат')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def agree(update, context):
    """agree"""
    update.message.reply_text('test')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1950363708:AAEHklSJsfyxonLdPwQ5zXw6H49X0oftmiQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("piracy", piracy))
    dp.add_handler(CommandHandler("agree", agree))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
