from xml.dom import minidom
from pathlib import Path


ar_path = Path('RIK_project/data/ar_names_list_types.txt')

def init_ar():
    if not ar_path.exists():
        names = extract_etv_names('RIK_project/data/ariregister/ettevotja_rekvisiidid_2022-03-29.xml')
        with open(ar_path, 'w') as file:
            file.write("\n".join(names))

def get_ar_names():
    with open(ar_path) as f:
        names = f.read().splitlines()
    return [name.strip() for name in names]

#Should this func actually remove these stopwords? - no
def strip_stopwords(trg_name: str):
    stopwords = ['oü', 'osaühing', 'täisühing', 'tü', 'aktsiaselts', 'as', 'usaldusühing', 'uü', 'ühistu']
    trg_name = trg_name.lower()
    for sw in stopwords:
        if sw in trg_name:
            return trg_name.replace(sw, '').strip()
    return trg_name


def extract_etv_names(xml_path):
    etv_name_list = []
    xmldoc = minidom.parse(xml_path)
    etvs = xmldoc.getElementsByTagName('ettevotja')

    for child in etvs:
        etv_name = child.getElementsByTagName('nimi')[0].firstChild.nodeValue
        state = child.getElementsByTagName('ettevotja_staatus')[0].firstChild.nodeValue
        if state == 'R':
            etv_name_list.append(strip_stopwords(etv_name))
    return etv_name_list
