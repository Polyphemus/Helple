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

total_letters = 0

for word in fiversList:
    for chr in word:
        histoDict[chr] += 1
        total_letters += 1

for key in sorted(histoDict, key=histoDict.get, reverse=True):
    print(key + ': ' + "{:.2f}".format(histoDict[key]/total_letters*100))

