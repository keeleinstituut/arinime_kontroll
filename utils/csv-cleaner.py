# Cleans csv-file of unneccessary commas, parentheses, numberts, spaces at the beginning of name etc.
# Every placename is taken to newline
import os
from config.definitions import DATA_DIR
import re
import csv


with open(os.path.join(DATA_DIR, 'placenames', 'eestikohanimed.csv'), 'r') as file_r, open(os.path.join(DATA_DIR, 'placenames', 'kohanimed2.csv'), 'w', newline='') as file_w:
    writer = csv.writer(file_w)
    for line in file_r:
        if len(line) > 1:
            line = line.split(',')
            if len(line) > 1:
                for l in line:
                    if len(l) > 1:
                        l = re.sub('\(([0-9])*:', '', l)
                        l = re.sub('^\s', '', l)
                        line = ','.join(l)
                        writer.writerow([l])
            else:
                line[0] = re.sub('\(([0-9])*:', '', line[0])
                line[0] = re.sub('\n', '', line[0])
                writer.writerow([line[0]])

print('done')
