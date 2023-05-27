from transliterate import to_latin, to_cyrillic
async def krill_latin(word):
    if word.isascii():
        response = await to_cyrillic(word)
    else:
        response = await to_latin(word)

    return response