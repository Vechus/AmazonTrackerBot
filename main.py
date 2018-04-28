import telebot
#import logging
import sqlite3 as lite
import amazonRequest


database = lite.connect('devdatabase.db')
cur = database.cursor()

# FEEDBACK = 12
# logging.addLevelName(FEEDBACK, 'FEEDBACK')
# logging.basicConfig(filename='testing.log', filemode='w+', level=logging.DEBUG)

bot = telebot.TeleBot("577135328:AAEBSQdPZE3UO4aUqt_pAWrrbBaGTST1DRM")
print("Starting...")


# Start / Help
@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    bot.reply_to(message, "Hello, this bot allows you to track an Amazon product price by name, url or category.")


@bot.message_handler(commands=['feedback'])
def sendFeedback(message):
    bot.send_message(25370519, "[" + str(message.chat.first_name) + "](tg://user?id=" + str(message.chat.id) + "): " + message.text, parse_mode="Markdown")  # sostituire l'id con l'id di un canale per i feedback
    # logging.log(FEEDBACK, "from: " + str(message.chat.username) + ": " + message.text)
    bot.reply_to(message, "Feedback sent!")


@bot.message_handler(commands=['test'])
def testReq(message):
    if message.text.find('amazon.it', 0) == -1:
        bot.reply_to(message, "You didn't input an amazon.it url... Stupid fucking tester.")
    else:
        product_found = amazonRequest.requestPriceUrl(str(message.chat.username), message.text, cur)
        if product_found:
            bot.reply_to(message, """Found a product, it's in "crypted" database""")
        else:
            bot.reply_to(message, "The product has been found, but the dev is too lazy to implement new cases, I'm sorry.")


# Not implemented / not a command / bugged
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text + " is not a command.")


# START BOT
print("Bot started.")
bot.polling()
