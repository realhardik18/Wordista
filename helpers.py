import requests

def GetMeaning(word):
    response=requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    data={}
    data['word']=response[0]['word']
    data['POS']=response[0]['meanings'][0]['partOfSpeech']
    data['definition']=response[0]['meanings'][0]['definitions'][0]['definition']
    return data
print(GetMeaning('solution'))