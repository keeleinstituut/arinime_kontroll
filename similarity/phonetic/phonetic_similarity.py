from utils.arireg_processor import get_ar_names
from utils.arireg_processor import strip_stopwords
from .soundex import EstonianSoundex
from .distance import PhoneticsInnerLanguageDistance
from .metaphone import EstonianMetaphone



def calculate_similarity(name_a: str, name_b: str):
    #soundex = EstonianSoundex()
    metaphone = EstonianMetaphone()
    #soundex_distance = PhoneticsInnerLanguageDistance(soundex)
    metaphone_distance = PhoneticsInnerLanguageDistance(metaphone)

    #soundex_score = 100.0 - min(soundex_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00
    metaphone_score = 100.0 - min(metaphone_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00

    return metaphone_score


def calculate_phon_sim(input_name: str):
    stripped_input_name = strip_stopwords(input_name)
    ARIREGISTER = get_ar_names()
    similarities = []
    for comp_name in ARIREGISTER:
        stripped_comp_name = strip_stopwords(comp_name)
        similarity_score = calculate_similarity(stripped_input_name, stripped_comp_name)
        if similarity_score > 80:
            similarity = {
                'nimi': comp_name,
                'sarnasus_skoor': similarity_score
            }
            similarities.append(similarity)
    similarities = sorted(similarities, key=lambda d: d['sarnasus_skoor'], reverse=True)
    return similarities

def prop_confs():
    return
