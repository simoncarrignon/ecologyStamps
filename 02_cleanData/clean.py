#!/usr/bin/python3

import re

# this script removes everything except for lat, long and code. The code only has alphabetic characters and all of them are finally transformed to uppercase.

sep = ';'
stamps = open("../01_querySample/stampsSimple.csv", "r")
output = open("stamps.csv", "w")
output.write("id"+sep+"lat"+sep+"long"+sep+"type"+sep+"site"+sep+"code\n")

listIds = list()
listStamps = list()    
listTypes = list()
listSites = list()

for stamp in stamps:
    stampParsed = stamp.split(';')
    idStamp = stampParsed[1]
    latStamp = stampParsed[6]
    longStamp = stampParsed[5]
    typeStamp = stampParsed[2]
    siteStamp = stampParsed[3]

    code = stampParsed[7]
    # transform to upper
    code = code.upper()
    # remove everything except for A-Z
    codeCleaned = re.sub(r'[^A-Z]+', '', code)
    # remove empty codes
    if not codeCleaned:
        continue

    if idStamp in listIds:
        index = listIds.index(idStamp)
        duplicatedCode = listStamps[index]
        if codeCleaned == duplicatedCode:
            continue
    
    # Attention! Only Dressel 20
#    if typeStamp != "Dressel 20":
#     continue

    listIds.append(idStamp)
    listStamps.append(codeCleaned)
    listTypes.append(typeStamp)
    listSites.append(siteStamp)
    output.write(idStamp+sep+latStamp+sep+longStamp+sep+typeStamp+sep+siteStamp+sep+codeCleaned+'\n')

stamps.close()
output.close()


