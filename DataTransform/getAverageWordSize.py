from numpy import average

from DataGathering.sanitizeString import sanitizeString


def calculateAverageWordSize(text):
    textSplit = sanitizeString(text).split()

    return average([len(word) for word in textSplit])

def getAverageWordSize(df):
    return df['Discurso'].map(lambda d: calculateAverageWordSize(str(d)))

# print(string_to_test)
# print(calculateAverageWordSize(string_to_test))
