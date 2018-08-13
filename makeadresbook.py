#!usr/bin/python3
"""
Author: Thijs Maas
"""
import os
import re

def cardreader(filename):
    """reads a cardfile, yields records"""
    with open(filename) as fo:
        records = fo.read().split("BEGIN:VCARD")
        for record in records[1:]:
            yield record

def recordreader(record):
    """reads a record, return the name and phonenumber"""
    phone = "not found"
    for line in record.split("\n"): 
        if findname(line):
            name = findname(line)
        if findphone(line):
            phone = findphone(line)

    return name, phone

def findname(line):
    """Finds name"""
    if line.startswith("FN:"):
        return line.split("FN:")[-1]
    else:
        return False

def findphone(line):
    """Finds phonenr, prefer the return the nr with landcode"""
    pattern1 = re.compile(r'([+]3\d\s6\s\d{8})') #This pattern does not work on 06 numbers
    pattern2 = re.compile(r'\d{8}')
    match1 = pattern1.search(line)
    match2 = pattern2.search(line)
    if match1:
        return match1.group(0)
    elif match2:
        return match2.group(0)
    return False

def writebook(adresbook):
    """write dict to a file"""
    with open("adresbook.txt", 'w') as w:
        for k, v in adresbook.items():
            print(k, v, sep='\t', file=w)
        

if __name__ == "__main__":

    # read all .vcf files and make into a single file for easy dictionary
    adresbook = {}
    path = "/media/thijs/Storage/Projects/whatsapp/whatsappchatwithdetheijsapp/"
    for f in os.listdir(path):
        if f.endswith(".vcf"):
            filename = os.path.join(path, f)
            for record in cardreader(filename):
                name, phone = recordreader(record)
                adresbook[phone] = name
    
    writebook(adresbook)
