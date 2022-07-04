import webbrowser
import requests
from speech_recognition import Recognizer, Microphone

from System.DefaultCommands import random_sentence, random_jokes, OpenLink, SearchGoogleAutomatically
from System.TalkWithMe import TalkAutoResponse
from System.sys import not_response, sayWithVoice, SelectorResponse


class Falcon:
    def __init__(self):
        r = Recognizer()
        keyword = ['recherche', 'google', 'ouvre', 'phrase', 'aléatoire', 'raconte', 'blague', 'dis']
        basic_sentence = [['tu vas bien', 'vous allez bien', 'comment vas-tu'],
                          ['je t\'aime', 'tu es belle', 'tu es beau'], 'vien on se marie']

        # all_keys = [basic_sentence, keyword]

        keyword_referencies = {
            (keyword[0], keyword[0]): SearchGoogleAutomatically,
            (keyword[2], keyword[2]): OpenLink,
            (keyword[3], keyword[4]): random_sentence,
            (keyword[5], keyword[6]): random_jokes,
            (keyword[7], keyword[6]): random_jokes,
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
                        if 'ouvre' in response.lower():
                            keyword_referencies.get(key)(response.split(' ', 1)[1])
                        else:
                            keyword_referencies.get(key)()

                        break
                else:
                    if response.lower() not in key:
                        self.counter_false_response += 1

                if response.lower() in basic_sentence[0]:
                    SelectorResponse(0)
                elif response.lower() in basic_sentence[1]:
                    SelectorResponse(1)
                elif response.lower() in basic_sentence[2]:
                    SelectorResponse(2)
                else:
                    self.counter_false_response += 1

                if self.counter_false_response >= 2:
                    not_response()  # System talk automatique avec OpenAI
                    self.counter_false_response = 0

                """for k in keyword_referencies:
                    if k in response.lower():
                        keyword_referencies.get(k)"""


            except Exception as e:
                print(e)
