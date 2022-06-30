from deep_translator import GoogleTranslator
from blagues_api import BlaguesAPI, BlagueType
from essential_generators import DocumentGenerator
import requests


def display_Crypto():
    url = 'https://rest.coinapi.io/v1/orderbooks/current?filter_symbol_id=1'
    headers = {'X-CoinAPI-Key': 'D8AB730B-906E-4EC1-9E81-D701D189D915'}
    response = requests.get(url, headers=headers)

    print(response.text)

    # of bitcoin on real time !


def random_sentence():
    gen = DocumentGenerator()
    to_translate = gen.sentence()

    translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)

    print(f"> {translated}")


def random_jokes(self=None):
    blague = BlaguesAPI.random(self=self)
    print(blague)
