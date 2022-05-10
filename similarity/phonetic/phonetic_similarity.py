from utils.arireg_processor import get_ar_names
from .soundex import EstonianSoundex
from .distance import PhoneticsInnerLanguageDistance
from .metaphone import EstonianMetaphone


def calculate_similarity(name_a: str, name_b: str):
    soundex = EstonianSoundex()
    metaphone = EstonianMetaphone()
    soundex_distance = PhoneticsInnerLanguageDistance(soundex)
    metaphone_distance = PhoneticsInnerLanguageDistance(metaphone)

    soundex_score = 100.0 - min(soundex_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00
    metaphone_score = 100.0 - min(metaphone_distance.distance(name_a, name_b), len(name_a)) / len(name_a) * 100.00

    return max(soundex_score, metaphone_score)


def calculate_phon_sim(input_name: str):
    ARIREGISTER = get_ar_names()
    similarities = []
    for comp_name in ARIREGISTER:
        similarity_score = calculate_similarity(input_name, comp_name)
        if similarity_score > 90:
            similarity = {
                'nimi': comp_name,
                'sarnasus_skoor': similarity_score
            }
            similarities.append(similarity)
    return similarities

def prop_confs():
    return
