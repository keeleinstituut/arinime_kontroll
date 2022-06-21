from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from utils.morpher import get_lemma, tokenize, check_unknown
from final_score.checker import name_check

#res = calculate_phon_sim('tere')
#print(res)

#print(get_lemma('kõik'))
#print(tokenize('Ilus part kolksus koos!'))
#print(check_unknown('frikadel'))

print(name_check('tere', '23'))