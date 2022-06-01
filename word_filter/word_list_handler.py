
def get_list(l_type, lang):
    word_list = open(f"RIK_project/data/{l_type}/{lang}/wordlist.csv").read().split()
    return word_list

def add_to_list(new_word, lang, list_type):
    with open(f"RIK_project/data/{list_type}/{lang}/wordlist.csv", 'a') as f:
        f.write(new_word)

def remove_from_list(removed_word, list_type):
    pass