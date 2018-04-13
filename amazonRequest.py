import requests
import logging
from bs4 import BeautifulSoup

def requestPriceUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    nomeProdotto = soup.find("span", {"id": "productTitle"})
    nomeProdotto_text = " ".join(nomeProdotto.text.split())
    # TODO-vechus implement all cases
    prezzo = soup.find("span", {"id": "priceblock_saleprice"})
    prezzo_text = prezzo.text


