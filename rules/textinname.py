from estnltk import Text
import unicodedata as ud
# ãèøćĒķ Eesti õäöüzžwšsfxy

ET_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'š', 'z',
               'ž', 't', 'u', 'v', 'w', 'õ', 'ä', 'ö', 'ü', 'x', 'y', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&',
               '-', '.', '!', '?', ',', '_', ' ']
selectedname = "Tõ%re Kartul OÜ"
OY = ["OÜ", "osaühing", "Osaühing"]
TY = ["TÜ", "täisühing", "Täisühing"]
UY = ["UÜ", "usaldusühing", "Usaldusühing"]
AS = ["AS", "aktsiaselts", "Aktsiaselts"]
FIE = ["FIE", "füüsilisest isikust ettevõtja", "Füüsilisest Isikust Ettevõtja"]
TYPES = OY + TY + UY + AS + FIE
#takennames = ["Punased Kapsad aktsiaselts", "Punased Kapsad Osaühing", "Tore Kartul OÜ", "Stuudio AS", "Punakad Kapsad aktsiaselts"]

# checks if field is empty
def checkifempty(selectedname):
    # checks if selectedname is not empty
    if selectedname != None and len(selectedname) > 0:
        resulttext = typeinname(selectedname)
    else:
        resulttext = "Palun sisesta ärinimi."
    return resulttext

# checks if chosen name constists of name and type
def typeinname(selectedname):
    #checks if there is only one business type specified in name
    splitname = selectedname.split(" ")
    if "füüsilisest isikust ettevõtja" in selectedname.lower():
        splitname.append("füüsilisest isikust ettevõtja")
    if len([x for x in splitname if x in TYPES]) > 1:
        resulttext = "Nimes tohib esineda vaid üks õiguslik vorm"
    
    else:
        # checks if selectedname has both name and type
        if  selectedname in TYPES:
            resulttext = "Nimi ei saa koosneda vaid viitest õiguslikule vormile."
        
        # checks if selectedname has correct type
        elif "füüsilisest isikust ettevõtja" in selectedname.lower():
            resulttext = "Ettevõtte nimekuju on korrektne."
        else:
            splitname = selectedname.split(" ")
            compname = []
            compname.extend([splitname[0], splitname[-1]])

            # checks if selectedname has correct type
            if any(typetext in compname for typetext in TYPES):
                resulttext = "Ettevõtte nimekuju on korrektne."
            else:
                resulttext = "Ettevõtte tüüp ei ole nimes õigesti määratud (viide sedadusele, kontrolli õigekirja vmt)"

    return resulttext
#tulemus = typeinname(selectedname, TYPES)
#print(tulemus)

# checks if words "Eesti, riigi, valla, linna" are present in name
def wordsinname(selectedname):
    nametext = Text(selectedname)
    nametext.tag_layer(['morph_analysis'])
    resulttext = nametext.morph_analysis.lemma
    flattext = [item for sublist in resulttext for item in sublist]
    notallowed_list = ['Eesti', 'riik', 'vald', 'linn']
    if any(word in flattext for word in notallowed_list):
        resulttext = "§ 12(6) Sõnu «riigi» või «linna» või «valla» või muid riigi või kohaliku omavalitsusüksuse osalusele viitavaid sõnu võib äriühingu ärinimes kasutada ainult siis, kui riigile või kohalikule omavalitsusele kuulub üle poole ühingu osadest või aktsiatest."
        return False, resulttext
    else:
        resulttext = "Ettevõtte nimekuju on korrektne."
        return True, resulttext

#tulemus = wordsinname(selectedname, TYPES)
#print(tulemus)

# checks if the name is written in latin alphabet NB! includes all latin characters, incl. special chars like ãèø
def alphabet(selectedname):
    resulttext = "Ettevõtte nimekuju on korrektne."
    for char in selectedname:
        if char.lower() not in ET_alphabet:
            resulttext = "§ 12(8) Ärinimi peab olema kirjutatud eesti-ladina tähestikus."
            return False, resulttext
    return True, resulttext



