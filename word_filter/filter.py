from fuzzysearch import find_near_matches
from word_filter.word_list_handler import get_list
from word_filter.helper import morfer


def morph_expand(word_list):
    return [morfer(x) for x in word_list]


def find_bad_words(input_word, b_w_list):
    res = []
    for bword in b_w_list:
        f = find_near_matches(bword, input_word, max_l_dist=1)
        if len(f) > 0:
            res.append((f[0].matched, bword))
    return res


def replace_num_sym():
    pass


#API method
def filter_word(word):
    # tokenize incoming comp name

    # lemmatize all words

    # check every token
    list_check = find_bad_words(word, get_list('greylists', 'est'))
    list_check += find_bad_words(word, get_list('blacklists', 'est'))
    if len(list_check) > 0:
        return list_check, 'Nimi sisaldab ebasobilikku sõna'
    else:
        return [], 'Nimi ei sisalda ebasobilikke sõnu'
