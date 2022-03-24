import csv
from unittest import result
from attr import field
from estnltk import Text
import itertools

selectedname = "Suure Munamäe puhkekeskus OÜ"
OY = ["OÜ", "osaühing", "Osaühing"]
TY = ["TÜ", "täisühing", "Täisühing"]
UY = ["UÜ", "usaldusühing", "Usaldusühing"]
AS = ["AS", "aktsiaselts", "Aktsiaselts"]
FIE = ["FIE", "füüsilisest isikust ettevõtja", "Füüsilisest Isikust Ettevõtja"]
TYPES = OY + TY + UY + AS + FIE


# gives warning if is location is not accompanied by a modifyer, for exapmle "Suure Munamäe OÜ" does not pass while "Suure Munamäe puhkekeskus OÜ" is valid
def location(selectedname, TYPES):
    resulttext = "Nimi on korrektne."

    selectedname = selectedname.lower()
    splitname = selectedname.split(" ")
    typetext = ['füüsilisest', 'isikust', 'ettevõtja']
    
    for t in TYPES:
        typetext.append(t.lower())

    # cleans typetext from name, lemmatizes name
    splitname = [e for e in splitname if e not in typetext]
    joinedname = ' '.join(splitname)
    nametext = Text(joinedname)
    nametext.tag_layer(['morph_analysis'])
    nametext = nametext.morph_analysis.lemma
    nametext = ' '.join(list(itertools.chain.from_iterable(nametext)))
    #print(nametext)

    breakflag = False
    with open('placenames\kohanimed-puhas.csv', 'r', newline='') as file_r:
        reader = csv.reader(file_r, delimiter=',')
        for row in reader:
            for field in row:
                if field.lower() == nametext:
                    #print(field, nametext)
                    resulttext = "Nimes on kohanimi."
                    breakflag = True
                    break
            if breakflag:                   
                break       

    return resulttext

#print(location(selectedname, TYPES))
location(selectedname, TYPES)
