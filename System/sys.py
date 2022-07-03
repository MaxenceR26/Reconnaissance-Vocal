from random import randint

from pyttsx3 import init

engine = init('sapi5')


def SelectorResponse(id):
    a_lot_response = [
        [
            "Je vais bien c'est gentil de demander. Et vous, vous allez bien?",
            "Ohh que c'est gentil ! En effet tout va pour le mieux.",
            'Je vais bien merci.'
        ],
        [
            "Vous me dites des mots d'amour, des mots de tous les jours et... Attendez ça me rappelle quelque chose.",
            "C'est gentil.",
        ],
        [
            "Vous me dites des mots d'amour, des mots de tous les jours et... Attendez ça me rappelle quelque chose.",
            "Mon contrat de licence d'utilisateur final ne couvre pas le mariage.",
            "Allons bon... Regardez un oiseau ! Enfin bon, voilà quoi.",
            "Je veux bien.. Mais vous payez tous !"
        ]
    ]
    response = a_lot_response[id][randint(0, len(a_lot_response[id]) - 1)]
    print(">", response)
    sayWithVoice(response)


def not_response():
    sentence = [
        "Je n\'ai malheuresement aucune réponse à cela.",
        "Désolé cela dépasse de mes compétences."
    ]
    response = sentence[randint(0, len(sentence) - 1)]
    print(f"> {response}")
    sayWithVoice(response)


def sayWithVoice(text: str):
    engine.say(text)
    engine.runAndWait()
