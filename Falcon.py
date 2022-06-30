import webbrowser
from random import randint

import pyttsx3
import requests
from speech_recognition import Recognizer, Microphone

from System.DefaultCommands import random_sentence, random_jokes
from System.sys import not_response, sayWithVoice, SelectorResponse

engine = pyttsx3.init()


class Falcon:
    def __init__(self):
        r = Recognizer()
        keyword = ['recherche', 'google', 'ouvre', 'phrase', 'aléatoire', 'raconte', 'blague']
        basic_sentence = [['tu vas bien', 'vous allez bien', 'comment vas-tu'],
                          ['je t\'aime', 'tu es belle', 'tu es beau'], 'vien on se marie']

        keyword_referencies = {
            keyword[0]: SearchGoogleAutomatically,
            keyword[2]: OpenLink,  # A réaliser
            (keyword[3], keyword[4]): random_sentence,
            (keyword[5], keyword[6]): random_jokes
        }
        with Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sayWithVoice("Oui dis-moi ?")
            audio = r.listen(source)
            try:
                response = r.recognize_google(audio, language="fr-FR")

                print(f"\nDis Falcon, {response} >")

                """for key in basic_sentence[0]:
                    if key in response.lower():
                        response = same_response[randint(0, len(same_response) - 1)]
                        print(">", response)
                        sayWithVoice(response)"""

                self.counter_false_response = 0

                for key in keyword_referencies:
                    if not any([word for word in key if word not in response.lower()]):
                        keyword_referencies.get(key)()

                """for i in basic_sentence:
                    for k in range(len(basic_sentence)):
                        if not any([word for word in i[k] if word not in response.lower()]):
                            SelectorResponse(k)"""  # Fonctionnel mais a modifié

                match response.lower():
                    case basic_sentence[0]:
                        

                """if response.lower() in basic_sentence[0]:
                    SelectorResponse(0)
                elif response.lower() in basic_sentence[1]:
                    SelectorResponse(1)
                elif response.lower() in basic_sentence[2]:
                    SelectorResponse(2)
                else:
                    self.counter_false_response += 1
                    if self.counter_false_response >= 2:
                        not_response()"""


                """for k in keyword_referencies:
                    if k in response.lower():
                        keyword_referencies.get(k)"""


            except Exception as e:
                print(e)


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
            elif requests.get(f"https://{args}.fr"):
                webbrowser.open(f"https://{args}.fr")
        except:
            pass
