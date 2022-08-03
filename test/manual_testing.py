from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from utils.morpher import get_lemma, tokenize, check_unknown
from final_score.checker import name_check
import os
from config.definitions import ROOT_DIR, DATA_DIR

res = calculate_phon_sim('xr oü')
print(res)

#print(get_lemma('kõik'))
#print(tokenize('Ilus part kolksus koos!'))
#print(check_unknown('frikadel'))

#print(name_check('tere', '23'))

print(DATA_DIR)