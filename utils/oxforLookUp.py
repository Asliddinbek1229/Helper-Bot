import requests

app_id = "c64b01ef"
app_key = "02027f4d5d590e090e6d848e3f08330a"
language = "en-gb"

async def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']:
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output