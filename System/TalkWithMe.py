import openai
from deep_translator import GoogleTranslator

from System.sys import sayWithVoice


def TalkAutoResponse(text):
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You: {text}",
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
        new_translated = f"> {translated}".replace('?\n\n', '')
        print(new_translated)
        if '-' in new_translated[0]:
            print("> {}".format(new_translated.replace(new_translated[0], '')))
            sayWithVoice(translated.replace('?\n\n', ''))
    else:
        print("{}".format(translated.split()[0].join('>> ')), end='')
        sayWithVoice(translated)

