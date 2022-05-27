import csv
from unittest import result
from estnltk import Text
import itertools

#selectedname = "Suure Munamäe puhkekeskus OÜ"
OY = ["OÜ", "osaühing", "Osaühing"]
TY = ["TÜ", "täisühing", "Täisühing"]
UY = ["UÜ", "usaldusühing", "Usaldusühing"]
AS = ["AS", "aktsiaselts", "Aktsiaselts"]
FIE = ["FIE", "füüsilisest isikust ettevõtja", "Füüsilisest Isikust Ettevõtja"]
TYPES = OY + TY + UY + AS + FIE


# gives warning if is location is not accompanied by a modifyer, for exapmle "Suure Munamäe OÜ" does not pass while "Suure Munamäe puhkekeskus OÜ" is valid
def location(selectedname):
    resulttext = "Nimi on korrektne."

    selectedname = selectedname.lower()
    splitname = selectedname.split(" ")
    typetext = ['füüsilisest', 'isikust', 'ettevõtja']
    
    for t in TYPES:
        typetext.append(t.lower())
    
    # cleans typetext from name, lemmatizes name
    splitname = [e for e in splitname if e not in typetext]
    joinedname = ' '.join(splitname)
    namelemmas = Text(joinedname)
    namelemmas.tag_layer(['morph_analysis'])
    namelemmas = namelemmas.morph_analysis.lemma
    print(namelemmas)
    joinednamelemmas = ' '.join(list(itertools.chain.from_iterable(namelemmas)))
    print(namelemmas)

    # leiab nüüd kõik kohanimed, ka siis, kui on täiend nimes olemas
    namelist = []
    for el in splitname:
        namelist.append(el)
    namelist.append(joinedname)
    for el in namelemmas:
        for e in el:
            namelist.append(e)   
    print(namelist)


    breakflag = False
    
    with open('RIK_project/data/placenames/kohanimed.csv', 'r', newline='') as file_r:
        reader = csv.reader(file_r, delimiter=',')
        #counter = 0
        for row in reader:
            #counter += 1
            for field in row:
                if field.lower() in namelist:
                    #print(counter)
                    placename = 'Nimes sisaldub kohanimi "' + str(field)+'".'
                    resulttext = str(placename) + " § 12.(5) Kui ärinimi lisaks äriühingule viitavale täiendile sisaldab riigi, haldusüksuse või muu koha nime, peab ärinimi sisaldama riigi, haldusüksuse või muu koha nimest eristavat täiendit. \n§ 12.(6) Ärinimes ei või kasutada riigi või kohaliku omavalitsuse organite ja asutuste nimetusi. \n§ 8.(2) Füüsilisest isikust talupidaja ärinimi ei pea sisaldama ettevõtja ees- ja perekonnanime juhul, kui ärinimes sisaldub talu nimi."
                    breakflag = True
                    break
            if breakflag:                   
                break
                   

    return resulttext