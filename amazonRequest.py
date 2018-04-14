import requests
import logging
from bs4 import BeautifulSoup

def requestPriceUrl(chat_id, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    product_name = soup.find("span", {"id": "productTitle"})
    product_name_text = " ".join(product_name.text.split())
    # TODO-vechus implement all cases
    price = soup.find("span", {"id": "priceblock_saleprice"})
    price_text = prezzo.text


