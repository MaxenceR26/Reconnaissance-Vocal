"""import openai

from deep_translator import GoogleTranslator

from System.sys import sayWithVoice

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-002",
    prompt="You: Récite moi un poème",
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You : "]
)
translated = GoogleTranslator(source='auto', target='fr').translate(
    response['choices'][0]['text'].replace('\n\n.L\'autre personne : ', ''))
vanish = "?\n\n"
if vanish:
    print("> {}".format(translated.replace('?\n\n', '')))
    sayWithVoice(translated.replace('?\n\n', ''))
else:
    print("> {}".format(translated))
    sayWithVoice(translated)"""


"""def test1():
    print("test1")

def test2():
    print("test2")

def test3():
    print("test3")

def test4():
    print("test4")

def test5():
    print("test5")

keyword = ['recherche', 'google', 'ouvre', 'phrase', 'aléatoire', 'raconte', 'blague', 'dis']

# all_keys = [basic_sentence, keyword]

keyword_referencies = {
    (keyword[0], keyword[0]): test1,
    (keyword[2], keyword[2]): test2,  # A réaliser
    (keyword[3], keyword[4]): test3,
    (keyword[5], keyword[6]): test4,
    (keyword[7], keyword[6]): test5,
}

response = "recherche-moi une phrase aléatoire"

for key in keyword_referencies:
    if not any([word for word in key if word not in response.lower()]):
        keyword_referencies.get(key)()
        break"""