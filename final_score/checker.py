from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from similarity.textual_similarity import calculate_text_sim
from rules.location_in_name_checker import location
from rules.textinname import wordsinname, alphabet, ET_alphabet
from trademarks.trademark_check import et_trademark_check
from word_filter.filter import filter_word
from word_filter.word_list_handler import get_list


def name_check(bis_name, bis_domain):
    result_message = ''
    pho_sim = calculate_phon_sim(bis_name)
    module_name = ''
    if not pho_sim == []:
        result_message += 'Liiga sarnane häälduselt eelnevalt registreeritud ärinimedele!; '
        module_name += 'Foneetiline; '

    txt_sim = calculate_text_sim(bis_name)
    if not txt_sim == []:
        result_message += 'Liiga sarnane kirjapildilt eelnevalt registreeritud ärinimedele!; '
        module_name += 'Tekstiline; '

    filter_words, filter_msg = filter_word(bis_name)
    if not filter_words == []:
        result_message += filter_msg + '; '
        module_name += 'Filter; '

    trademark_res, trademark_msg, collected_trademarks = et_trademark_check(bis_name, bis_domain)
    if not trademark_res:
        result_message += trademark_msg + '; '
        module_name += 'Kaubamärk; '

    loc_res, loc_msg = location(bis_name)
    if not loc_res:
        result_message += loc_msg + '; '
        module_name += 'Kohanimi; '

    wdn_res, wdn_msg = wordsinname(bis_name)
    if not wdn_res:
        result_message += wdn_msg + '; '
        module_name += 'Riiklik; '

    alph_res, alph_msg = alphabet(bis_name)
    if not alph_res:
        result_message += alph_msg + '; '
        module_name += 'Tähestik; '

    return 0, result_message, module_name
