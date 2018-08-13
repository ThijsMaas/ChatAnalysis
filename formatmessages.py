#!usr/bin/python3
"""
Author: Thijs Maas
"""
import re

def splitmessages(chatfile):
    """open the chatfile and splits the txt in seperate messages, 1 string per message"""
    p = re.compile(r'^(\d\d/\d\d/\d\d\d\d, \d\d:\d\d -)')
    L = []
    with open(chatfile, 'r') as f:
        for line in f.readlines():
            match = p.search(line)
            if match:
                L.append(line.strip("\n"))
            else:
                L[-1] = L[-1]+" "+line.strip("\n")
    for i in L:
        yield i
            
def messagemaker(messageline):
    """Takes a message and extracts the date, time and author"""
    p = re.compile(r'(\d\d/\d\d/\d\d\d\d), (\d\d:\d\d) - (.+?(?= left| added|:| changed| removed| joined))[:\s]{1,2}(.*)') 
    match = p.search(messageline)
    if match:
        message = match.group(1, 2, 3, 4)
        message = [m.strip("\u202a").strip("\u202c") for m in message]
        return message
    else:
        print("No match found here:", messageline, sep='\n')

def main(chatfile):
    c = 1
    for line in splitmessages(chatfile):
        c += 1
        message = messagemaker(line)
        yield message
    print(c,"messages found")

if __name__ == "__main__":
    # adresbook not used anymore
    # adresbook = {}
    # with open("adresbook.txt") as abfile:
    #     for adres in abfile.readlines():
    #         phone, name = adres.split('\t')
    #         name = name.strip("\n")
    #         adresbook[phone] = name
    pass