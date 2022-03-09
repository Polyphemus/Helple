#! Python 3

# Cheats at Wordle

import string


dictFile = open('Dict.txt')
dictList = dictFile.readlines()
histoDict = dict.fromkeys(string.ascii_lowercase, 0)
total_letters = 0

fiversList = []

for word in dictList:
    if len(word) == 6:
        fiversList.append(word[0:5])

febTenWords = []
for word in fiversList:
    if word[3] == 's' and word[4] == 'e' and 'r' not in word and 'i' not in word and 'a' in word and word[0] != 'a':
        febTenWords.append(word)
        print(word)

for word in febTenWords:
    for chr in word:
        histoDict[chr] += 1
        total_letters += 1

for key in sorted(histoDict, key=histoDict.get, reverse=True):
    print(key + ': ' + "{:.2f}".format(histoDict[key]/total_letters*100))
