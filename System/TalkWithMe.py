import openai
from deep_translator import GoogleTranslator


from System.sys import sayWithVoice


def TalkAutoResponse(text):
    import openai

    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    r = response["choices"][0]["text"].split('.', 1)
    translated = GoogleTranslator(source='english', target='fr').translate(r[0])
    print("> {}".format(translated.replace('?\n\n', '')))



