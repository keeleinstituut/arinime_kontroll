from fuzzysearch import find_near_matches
from .helper import morfer


def morph_expand(word_list):
    return [morfer(x) for x in word_list]


def get_list(l_type, lang, filename):
    word_list = open(f"data/{l_type}/{lang}/{filename}.csv").read().split()
    word_list = morph_expand(word_list)
    return word_list


def process(word, list_type):
    for bword in list_type:
        res = find_near_matches(bword, word, max_l_dist=1)
        if len(res) > 0:
            return res


def replace_num_sym():
    pass


def filter_word(word):
    greylist_check = process(word, get_list('greylists','est', 'hall_nimekiri'))
    blacklist_check = process(word, get_list('blacklists','est', 'must_nimekiri'))
    if len(greylist_check) > 0:
        return greylist_check[0].matched, 'Nimi sisaldab ebasobilikku sõna'
    elif len(blacklist_check) > 0:
        return blacklist_check[0].matched, 'Nimi sisaldab ebasobilikku sõna'
    else:
        return [], 'Nimi ei sisalda ebasobilikke sõnu'

