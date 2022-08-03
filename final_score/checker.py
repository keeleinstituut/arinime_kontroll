from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from similarity.textual_similarity import calculate_text_sim
from rules.location_in_name_checker import location
from rules.textinname import wordsinname, alphabet, ET_alphabet
from trademarks.trademark_check import et_trademark_check
from word_filter.filter import filter_word
from word_filter.word_list_handler import get_list
from final_score.score_calculator import calculate


def name_check(bis_name, bis_domain, modules=None, pho_thr=90, txt_thr=75):
    if modules is None:
        modules = ['A']
    result_message = ''
    errord_modules = ''
    pho_sim = 0
    txt_sim = 0
    if 'A' in modules or 'F' in modules:
        pho_sim = calculate_phon_sim(bis_name, pho_thr)
        if not pho_sim == []:
            result_message += 'Liiga sarnane häälduselt eelnevalt registreeritud ärinimedele!; '
            errord_modules += 'Foneetiline; '

    if 'A' in modules or 'T' in modules:
        print('In T')
        txt_sim = calculate_text_sim(bis_name, txt_thr)
        if not txt_sim == []:
            result_message += 'Liiga sarnane kirjapildilt eelnevalt registreeritud ärinimedele!; '
            errord_modules += 'Tekstiline; '

    if 'A' in modules or 'B' in modules:
        filter_words, filter_msg = filter_word(bis_name)
        if not filter_words == []:
            result_message += filter_msg + '; '
            errord_modules += 'Filter; '

    if 'A' in modules or 'K' in modules:
        trademark_res, trademark_msg, collected_trademarks = et_trademark_check(bis_name, bis_domain)
        if not trademark_res:
            result_message += trademark_msg + '; '
            errord_modules += 'Kaubamärk; '

    if 'A' in modules or 'L' in modules:
        loc_res, loc_msg = location(bis_name)
        if not loc_res:
            result_message += loc_msg + '; '
            errord_modules += 'Kohanimi; '

    if 'A' in modules or 'G' in modules:
        wdn_res, wdn_msg = wordsinname(bis_name)
        if not wdn_res:
            result_message += wdn_msg + '; '
            errord_modules += 'Riiklik; '

    if 'A' in modules or 'P' in modules:
        alph_res, alph_msg = alphabet(bis_name)
        if not alph_res:
            result_message += alph_msg + '; '
            errord_modules += 'Tähestik; '

    #score = calculate(pho_sim, txt_sim)
    score = 1
    return score, result_message, errord_modules, pho_sim, txt_sim
