import telebot
import logging
import simplejson
import amazonRequest

FEEDBACK = 12
logging.addLevelName(FEEDBACK, 'FEEDBACK')
logging.basicConfig(filename='testing.log', filemode='w+', level=logging.DEBUG)

bot = telebot.TeleBot("577135328:AAEBSQdPZE3UO4aUqt_pAWrrbBaGTST1DRM")
print("Starting...")

## Start / Help
@bot.message_handler(commands=['start','help'])
def sendWelcome(message):
    bot.reply_to(message, "Hello, this bot allows you to track an Amazon product price by name, url or category.")

@bot.message_handler(commands=['feedback'])
def sendFeedback(message):
    logging.log(FEEDBACK, "from: " + str(message.chat.username) + ": " + message.text)
    bot.reply_to(message, "Feedback sent!")

@bot.message_handler(commands=['test'])
def testReq(message):
    if message.text.find('amazon.it', 0) == -1:
        bot.reply_to(message, "You didn't input an amazon.it url... Stupid fucking tester.")
    else:
        product_found = {}
        product_found = amazonRequest.requestPriceUrl(str(message.chat.username), message.text)
        try:
            bot.reply_to(message, "Found a product, it is: " + product_found[0] + ", price: " + product_found[1] + "€.")
        except:
            bot.reply_to(message, "The product has been found, but the dev is too lazy to implement new cases, I'm sorry. but hey, at least I found it, here it is!")


## Not implemented / not a command / bugged
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text + " is not a command.")

##### START BOT #####
print("Bot started.")
bot.polling()
