from xml.dom import minidom
from os.path import exists


ee_trademarks_path = 'RIK_projects/data/kaubamargid_nimed/eki_eesti_kaubamargid_20220201.xlsx'

def init_ar():
    if not exists(ar_path):
        names = extract_etv_names('RIK_project/data/ettevotja_rekvisiidid_2022-01-26.xml')
        with open(ar_path, 'w') as file:
            file.write("\n".join(names))

def get_ar_names():
    with open(ar_path) as f:
        names = f.read().splitlines()
    return [name.strip() for name in names]