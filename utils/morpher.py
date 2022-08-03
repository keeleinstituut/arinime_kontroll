from estnltk import Text
from estnltk.default_resolver import make_resolver


def check_unknown(input_word):
    resolver_unk = make_resolver(
        disambiguate=False,
        guess=False,
        propername=False,
        phonetic=False,
        compound=True)
    print(Text(input_word).tag_layer(resolver=resolver_unk)['morph_analysis'][0].lemma)
    return None in Text(input_word).tag_layer(resolver=resolver_unk)['morph_analysis'][0].lemma


def get_lemma(input_word):
    lemma = Text(input_word).tag_layer()['morph_analysis'][0].lemma
    return lemma


def tokenize(input_data):
    words = Text(input_data).tag_layer().words.text
    return words


def num_to_est_word(number: str):
    numbrite_eesti_vasted = {
        1: 'üks',
        2: 'kaks',
        3: 'kolm',
        4: 'neli',
        5: 'viis',
        6: 'kuus',
        7: 'seitse',
        8: 'kaheksa',
        9: 'üheksa',
        0: 'null',
    }

    return numbrite_eesti_vasted[int(number)]


def normalize_bisnames(name: str, remove_numbers: bool = False, convert_numbers: bool = False):
    result = [name]
    #remove bis types

    #remove number
    if remove_numbers:
        num_removed = ''.join([i for i in name if not i.isdigit()])
        result.append(num_removed)

    if convert_numbers:
        converted_num_est_single_digit = ''.join([num_to_est_word(c) for c in name if c.isdigit()])
        # implement num2words lib for ET
        #converted_num_est_multi_digit =
        result.append(converted_num_est_single_digit)
    return result