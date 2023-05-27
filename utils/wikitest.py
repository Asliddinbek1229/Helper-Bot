import wikipedia

async def sendWiki(msg):
    wikipedia.set_lang('uz')

    try:
        res = wikipedia.summary(msg)
        return res
    except:
        return f"😕 {msg} mavzusidagi maqola topilmadi"