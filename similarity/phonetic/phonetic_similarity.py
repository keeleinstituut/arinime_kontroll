from utils.arireg_processor import get_ar_names
from .soundex import EstonianSoundex
from .distance import PhoneticsInnerLanguageDistance
from .metaphone import EstonianMetaphone
from utils.morpher import normalize_bisnames


def calculate_similarity(name_a: str, name_b: str):
    #print(name_b)
    soundex = EstonianSoundex()
    metaphone = EstonianMetaphone()
    soundex_distance = PhoneticsInnerLanguageDistance(soundex)
    metaphone_distance = PhoneticsInnerLanguageDistance(metaphone)

    soundex_score = 100.0 - min(soundex_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00
    metaphone_score = 100.0 - min(metaphone_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00

    #print(soundex_distance.distance(name_a, name_b))
    #print(metaphone_distance.distance(name_a, name_b))
    #print(soundex_score)
    #print(metaphone_score)
    #return max(soundex_score, metaphone_score)
    return soundex_score, metaphone_score

def calculate_phon_sim(input_name: str, pho_thr = 90):
    ARIREGISTER = get_ar_names(len(input_name))
    #print(ARIREGISTER)
    similarities = []
    for comp_name in ARIREGISTER:
        comp_name = normalize_bisnames(comp_name)[0]
        #print(comp_name)
        soundex_score, metaphone_score = calculate_similarity(input_name, comp_name)
        if soundex_score > pho_thr or metaphone_score > pho_thr:
            similarity = {
                'nimi': comp_name,
                'soundex_skoor': soundex_score,
                'metaphone_skoor': metaphone_score
            }
            similarities.append(similarity)
    return similarities

def prop_confs():
    return
