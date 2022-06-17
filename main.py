from fastapi import FastAPI
from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from similarity.textual_similarity import calculate_text_sim
import utils.arireg_processor as ar
from rules.location_in_name_checker import location
from rules.textinname import wordsinname, alphabet, ET_alphabet
from trademarks.trademark_check import et_trademark_check
from word_filter.filter import filter_word
from word_filter.word_list_handler import get_list
from final_score.checker import name_check
import configparser


config = configparser.RawConfigParser()
config.read('server_conf')
server_info = dict(config.items('server_info'))

app = FastAPI(
    title="Ärinimekontroll - {}-server {}".format(server_info['server_name'], server_info['server_number']),
)
ar.init_ar()


@app.get('/')
def get_index():
    return {'Message': "Ärinimekontroll {}-server {}".format(server_info['server_name'], server_info['server_number'])}

@app.post('/ärinime_kontroll')
def all_in_check(bis_name: str, bis_domain: str):
    skoor, otsus, allikas = name_check(bis_name, bis_domain)
    response = {
        'tõenäosus_skoor': skoor,
        'otsus': otsus,
        'kontroll_moodul': allikas
    }
    return response



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
async def check_bad_words(bis_name: str):
    result, message = filter_word(bis_name)
    response = {
        'otsus': result,
        'sonum': message
    }
    return response

@app.get('/kuva_xsonad')
def get_bad_words():
    return {
            'hall_nimekiri': get_list('greylists', 'est'),
            'must_nimekiri': get_list('blacklists', 'est')
    }


@app.post('/kaubamargid')
async def trademark(bis_name: str, bis_domain: str):
    result, message, collect_trademarks = et_trademark_check(bis_name, bis_domain)
    response = {
        'otsus': result,
        'sonum': (message, collect_trademarks)
    }

    return response


@app.post('/kohanimi')
async def location_rule(bis_name: str):
    response = {
        'otsus': location(bis_name)
    }
    return response


@app.post('/riiksona')
async def gov_word_rule(bis_name: str):
    response = {
        'otsus': wordsinname(bis_name)
    }
    return response


@app.post('/t2hestik')
async def alphabet_rule(bis_name: str):
    response = {
        'otsus': alphabet(bis_name)
    }
    return response


@app.get('/t2hestik')
def get_alphabet():
    return {'lubatud symbolid': ET_alphabet}
