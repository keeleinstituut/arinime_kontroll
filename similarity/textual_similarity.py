import difflib
from utils.arireg_processor import get_ar_names
from utils.arireg_processor import strip_stopwords


def calcualte_similarity(name_a: str, name_b: str):
    seq = difflib.SequenceMatcher(None, name_a, name_b)
    return seq.ratio() * 100
    #return seq.quick_ratio() * 100


def calculate_text_sim(input_name: str, txt_thr=70):
    ARIREGISTER = get_ar_names(len(input_name))
    similarities = []
    input_name = input_name.lower()
    print(txt_thr)
    for comp_name in ARIREGISTER:
        #print(comp_name)
        typelesscomp_name = strip_stopwords(comp_name)
        typelesscomp_name = typelesscomp_name.rstrip()
        typelesscomp_name = typelesscomp_name.lstrip()
        similarity_score = calcualte_similarity(input_name, typelesscomp_name)
        if similarity_score > txt_thr:
            similarity = {
                'nimi': comp_name,
                'sarnasus_skoor': int(similarity_score)
            }
            similarities.append(similarity)
    similarities = sorted(similarities, key=lambda d: d['sarnasus_skoor'], reverse=True)
    return similarities
