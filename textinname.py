from estnltk import Text
import unicodedata as ud

selectedname = "ãèøćĒķ Eesti õäöüzžwšsfxy"
OY = ["OÜ", "osaühing", "Osaühing"]
TY = ["TÜ", "täisühing", "Täisühing"]
UY = ["UÜ", "usaldusühing", "Usaldusühing"]
AS = ["AS", "aktsiaselts", "Aktsiaselts"]
FIE = ["FIE", "füüsilisest isikust ettevõtja", "Füüsilisest Isikust Ettevõtja"]
TYPES = OY + TY + UY + AS + FIE
#takennames = ["Punased Kapsad aktsiaselts", "Punased Kapsad Osaühing", "Tore Kartul OÜ", "Stuudio AS", "Punakad Kapsad aktsiaselts"]

# checks if field is empty
def checkifempty(selectedname, TYPES):
    # checks if selectedname is not empty
    if selectedname != None and len(selectedname) > 0:
        resulttext = typeinname(selectedname, TYPES)
    else:
        resulttext = "Palun sisesta ärinimi."
    return resulttext

# checks if chosen name constists of name and type
def typeinname(selectedname, TYPES):               
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
def wordsinname(selectedname, TYPES):
    nametext = Text(selectedname)
    nametext.tag_layer(['morph_analysis'])
    resulttext = nametext.morph_analysis.lemma
    flattext = [item for sublist in resulttext for item in sublist]
    notallowed_list = ['Eesti', 'riik', 'vald', 'linn']
    if any(word in flattext for word in notallowed_list):
        resulttext = "§ 12(6) Sõnu «riigi» või «linna» või «valla» või muid riigi või kohaliku omavalitsusüksuse osalusele viitavaid sõnu võib äriühingu ärinimes kasutada ainult siis, kui riigile või kohalikule omavalitsusele kuulub üle poole ühingu osadest või aktsiatest." 
    else:
        resulttext = "Ettevõtte nimekuju on korrektne."
    return resulttext
#tulemus = wordsinname(selectedname, TYPES)
#print(tulemus)

# checks if the name is written in latin alphabet NB! includes all latin characters, incl. special chars like ãèø
def alphabet(selectedname, TYPES):
    latin_letters= {}

    def is_latin(uchr):
        #print(ud.name(uchr))
        try: return latin_letters[uchr]
        except KeyError:
            return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

    def only_roman_chars(unistr):
        return all(is_latin(uchr)
            for uchr in unistr
            if uchr.isalpha())
    
    if only_roman_chars(selectedname) == True:
        resulttext = "Ettevõtte nimekuju on korrektne."
    else:
        resulttext = "§ 12(8) Ärinimi peab olema kirjutatud eesti-ladina tähestikus."
    return resulttext
#tulemus = alphabet(selectedname, TYPES)
#print(tulemus)


