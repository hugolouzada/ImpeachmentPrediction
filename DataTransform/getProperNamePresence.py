from DataGathering.sanitizeString import sanitizeString


def checkProperNamePresence(text,namesList):
    wordPresence = [word in namesList for word in sanitizeString(text).split()]

    return True in wordPresence

def getProperNamePresence(df, namesList):
    return df['Discurso'].map(lambda d: checkProperNamePresence(str(d),namesList))