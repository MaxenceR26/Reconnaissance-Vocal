import webbrowser

from deep_translator import GoogleTranslator
import pyjokes
from essential_generators import DocumentGenerator
import requests
from speech_recognition import Recognizer, Microphone
from System.sys import sayWithVoice, translation


def display_Crypto():
    url = 'https://rest.coinapi.io/v1/orderbooks/current?filter_symbol_id=1'
    headers = {'X-CoinAPI-Key': 'D8AB730B-906E-4EC1-9E81-D701D189D915'}
    response = requests.get(url, headers=headers)

    print(response.text)

    # of bitcoin on real time !


def random_sentence():
    gen = DocumentGenerator()
    to_translate = gen.sentence()
    translation(to_translate)


def random_jokes():
    joke = pyjokes.get_joke(language="en", category="all")
    translation(joke)


class SearchGoogleAutomatically:
    def __init__(self):
        r = Recognizer()
        with Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sayWithVoice("Que veux-tu rechercher ?")
            audio = r.listen(source)
            try:
                response = r.recognize_google(audio, language="fr-FR")
                r = response.replace(' ', '+')
                webbrowser.open(f"https://www.google.com/search?q={r}")

            except Exception as e:
                print(e)


class OpenLink:
    def __init__(self, args):
        try:
            if requests.get(f"https://{args}.com"):
                webbrowser.open(f"https://{args}.com")
                print(f"{args}.com a était ouvert !")
            elif requests.get(f"https://{args}.fr"):
                webbrowser.open(f"https://{args}.fr")
                print(f"{args}.com a était ouvert !")
        except:
            pass
