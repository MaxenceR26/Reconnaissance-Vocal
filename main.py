import os
import time
from random import randint

from speech_recognition import Recognizer, Microphone

from Falcon import Falcon
from System.sys import sayWithVoice


class Main:
    def __init__(self):
        r = Recognizer()
        with Microphone() as source:
            # For adjusting comprehension
            comprehension = ['dis sale conne', 'dis sale con', 'falcon']
            self.not_comprehensive_response = [
                "Je n'ai pas très bien compris...",
                'Une erreur est survenue...',
                "Un papillon est passé devant moi cela ma distrait, je n'ai donc pas plus comprendre.",
                "Désolée, je n'ai pas bien entendu ce que vous venez de dire. Pourriez-vous répéter ?",
                "Je n'ai pas compris. Pourriez vous répéter."
            ]

            r.adjust_for_ambient_noise(source)
            print("Pour lancer la reconnaissance vocale dites : dis Falcon...")
            audio = r.listen(source)
            try:
                response = r.recognize_google(audio, language="fr-FR")
                if response.lower() == "dis falcon" or response.lower() in comprehension:
                    Falcon()
                else:
                    self.comprehensive_sentence()
                    print(response)
            except Exception as e:
                self.comprehensive_sentence()
                print(e)

    def comprehensive_sentence(self):
        response = self.not_comprehensive_response[randint(0, len(self.not_comprehensive_response) - 1)]
        print(response)
        sayWithVoice(response)

Main()
