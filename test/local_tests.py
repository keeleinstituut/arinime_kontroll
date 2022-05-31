from similarity.phonetic.phonetic_similarity import calculate_phon_sim
from utils.morpher import get_lemma, tokenize, check_unknown

#res = calculate_phon_sim('tere')
#print(res)

print(get_lemma('kõik'))
print(tokenize('Ilus part kolksus koos!'))
print(check_unknown('frikadel'))