import requests
#import logging
from bs4 import BeautifulSoup
import sqlite3 as lite

#import sys


#USERREQUEST = 25
#logging.addLevelName(USERREQUEST, 'USER REQUEST: ')
#logging.basicConfig(filename='testing.log', filemode='w+', level=logging.DEBUG)

def requestPriceUrl(user, url, cur):
	r = requests.get(url.split("/test ")[1])
	soup = BeautifulSoup(r.text, "html.parser")
	product_name = soup.find("span", {"id": "productTitle"})
	product_name_text = " ".join(product_name.text.split())
	#logging.log(USERREQUEST, "from: " + user + ": product: " + product_name_text)

	# TODO-vechus implement all cases
	# saleprice case
	#try:
	print("Product found for " + user + ": " ,product_name_text)
	price = soup.find("span", {"id": "priceblock_ourprice"})
	database = lite.connect('devdatabase.db')
	cur = database.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS Products(Id INT, Title TEXT, Price TEXT)")
	#cur.execute("CREATE TABLE IF NOT EXISTS Users(Id INT, Users TEXT)")
	cur.execute("SELECT COUNT(Id) FROM Products")
	rows = cur.fetchall().pop()
	cur.execute("INSERT INTO Products VALUES(" + str(rows[0]) + ", '" + product_name_text + "', '" + price.text + "')")
	database.commit()
	database.close()
	print("Product: Title: ", product_name_text, " ||Price: ", price.text)
	return 1
	#except:
		#print("Error: ", sys.exc_info())
		#return 0
