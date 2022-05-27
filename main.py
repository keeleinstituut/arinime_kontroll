from fastapi import FastAPI
from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from similarity.textual_similarity import calculate_text_sim
import utils.arireg_processor as ar
from rules.location_in_name_checker import location
from rules.textinname import wordsinname, alphabet, ET_alphabet
from trademarks.trademark_check import et_trademark_check
from word_filter.filter import filter_word

app = FastAPI()
ar.init_ar()


@app.get('/')
def get_index():
    return {'Message': "Ärinimekontroll {}-server {}".format()}


@app.post('/foneetiline')
async def phonetic(bis_name: str):
    response = {
        'foneetiliselt sarnased nimed': calculate_phon_sim(bis_name)
    }
    return response


@app.post('/tekstiline')
async def textual(bis_name: str):
    response = {
        'tekstiliselt sarnased nimed': calculate_text_sim(bis_name)
    }
    return response


@app.post('/xsonad')
async def bad_words(bis_name: str):
    result, message = filter_word(bis_name)
    response = {
        'otsus': result,
        'sonum': message
    }
    return response


@app.post('/kaubamargid')
async def trademark(bis_name: str, bis_domain: str):
    result, message = et_trademark_check(bis_name, bis_domain)
    response = {
        'otsus': result,
        'sonum': message
    }

    return response


@app.post('/kohanimi')
async def location_rule(bis_name: str):
    response = {
        'otsus': location(bis_name),
        'sonum': location(bis_name)

    }
    return response


@app.post('/riiksona')
async def gov_word_rule(bis_name: str):
    response = {
        'otsus': wordsinname(bis_name),
        'sonum': wordsinname(bis_name)

    }
    return response


@app.post('/t2hestik')
async def alphabet_rule(bis_name: str):
    response = {
        'otsus': alphabet(bis_name),
        'sonum': alphabet(bis_name)

    }
    return response


@app.get('/t2hestik')
def get_alphabet():
    return {'alphabet': ET_alphabet}
