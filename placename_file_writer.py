# extracts placenames from gml (xml) file

from bs4 import BeautifulSoup
import csv
 
with open('placenames\eesti-kohanimed.gml', 'r') as f:
    data = f.read()
 
Bs_data = BeautifulSoup(data, "xml")
placenames = Bs_data.find_all('text')

f = open('placenames\eestikohanimed.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)
print(type(placenames))

for placename in placenames:
    writer.writerow([placename.get_text()])
    print(placename.get_text())

f.close()
print('DONE')
 
# osade nimede tekstis oli üleliigseid märke (nt "(1:", ")" jmt)
# nimedes esineb duplikaate