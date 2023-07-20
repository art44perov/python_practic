import requests
import json
from googletrans import Translator

def facking():
    translator = Translator()
    lang = 'en'
    str_query = "https://evilinsult.com/generate_insult.php?lang=" + lang + "&type=json"
    response = requests.get(str_query)
    if response.status_code == 200:
        stroke_s = json.loads(response.text)['insult']
        res = translator.translate(stroke_s, src='en', dest='ru')
        return res.text
    else:
        return "No connection..."
