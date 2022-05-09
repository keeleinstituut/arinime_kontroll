from fuzzysearch import find_near_matches


def get_list(l_type, lang):
    word_list = open(f"../data/{l_type}/{lang}/*.csv").read().split()
    return word_list


def process(word, list_type):
    for bword in list_type:
        res = find_near_matches(bword, word, max_l_dist=1)
        if len(res) > 0:
            return res


def replace_num_sym():
    pass


def filter_word(word):
    greylist_check = process(word, get_list('greylists','est'))
    blacklist_check = process(word, get_list('blacklists','est'))
    if len(greylist_check) > 0:
        return greylist_check[0].matched, 'Nimi sisaldab ebasobilikku sõna'
    elif len(blacklist_check) > 0:
        return blacklist_check[0].matched, 'Nimi sisaldab ebasobilikku sõna'
    else:
        return [], 'Nimi ei sisalda ebasobilikke sõnu'

