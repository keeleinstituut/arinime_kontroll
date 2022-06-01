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