from os.path import exists
import pandas as pd
import json
import os
from config.definitions import DATA_DIR

ee_trademarks_path = os.path.join(DATA_DIR, 'tm_list.json')


def init_tm():
    if not exists(ee_trademarks_path):
        names = extract_tm_names(os.path.join(DATA_DIR, 'kaubamargid_nimed', 'eki_eesti_kaubamargid_20220201.xlsx'))
        with open(ee_trademarks_path, 'w', encoding='utf-8') as file:
            json.dump(names, file, ensure_ascii=False)


def get_tm_names():
    with open(ee_trademarks_path, 'r', encoding='utf-8') as file:
        # file.write("\n".join(names))
        tms = json.load(file)
    return tms


def extract_tm_names(xml_path):
    tm_list = []
    df = pd.read_excel(xml_path)
    tms = df['nimi'].tolist()
    tm_class = df['klass'].tolist()
    for i in range(len(tms)):
        print(tm_class[i])
        tm_list.append({'tm': tms[i], 'class': tm_class[i]})

    return tm_list


init_tm()
