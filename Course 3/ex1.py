import re

fileName = "regex_sum_866135.txt"
file = open(fileName)

finalList = list()
for index in file :
    y = re.findall('[0-9]+',index)
    finalList = finalList + y


finalSUM = 0
for index2 in finalList :
    finalSUM = finalSUM + int(index2)

print(finalSUM)