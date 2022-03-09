#! Python 3

# Reads a dictionary text file in, extracts five letter words, counts letter frequency

import string
import pprint

dictFile = open('Dict.txt')
dictList = dictFile.readlines()
histoDict = dict.fromkeys(string.ascii_lowercase, 0)

fiversList = []

for word in dictList:
    if len(word) == 6:
        fiversList. append(word[0:5])

bads = list('tislance')

for word in fiversList:
    if word[3] == 'o' and 'r' in word and word[1] != 'r':
        if not any(char in word for char in bads):
            print(word)
