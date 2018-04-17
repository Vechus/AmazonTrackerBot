import requests
import logging
from bs4 import BeautifulSoup

USERREQUEST = 25
logging.addLevelName(USERREQUEST, 'USER REQUEST: ')
logging.basicConfig(filename='testing.log', filemode='w+', level=logging.DEBUG)

def requestPriceUrl(user, url):
    r = requests.get(url.split("/test ")[1])
    soup = BeautifulSoup(r.text, "html.parser")
    product_name = soup.find("span", {"id": "productTitle"})
    product_name_text = " ".join(product_name.text.split())
    logging.log(USERREQUEST, "from: " + user + ": product: " + product_name_text)
    # TODO-vechus implement all cases
    # saleprice case
    try:
        print("Product found for ", user, ": ", str(product))
        price = soup.find("span", {"id": "priceblock_ourprice"})
        product = [product_name_text, str(price)]
        return product
    except:
        print("Error. The product is NULL")
