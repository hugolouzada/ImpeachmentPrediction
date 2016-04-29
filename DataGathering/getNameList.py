from DataGathering.sanitizeString import sanitizeString


def getNameList():

    #names from http://assisbrasil.org/nomes.html
    file = open("../Data/ListaDeNomes.txt",'r')

    names = set()
    for line in file:
        lineNames =[sanitizeString(name) for name in line.strip().split()]

        for name in lineNames:
            if len(name)>2:
                names.add(name)

    return list(names)

# names = getNameList()
# print(len(names))
# for name in sorted(names):
#     print(name)