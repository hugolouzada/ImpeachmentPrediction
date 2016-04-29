from DataGathering.sanitizeString import sanitizeString


def getWordPresence(df,word):
    return df['Discurso'].map(lambda d: 'Has' if word in sanitizeString(str(d)) else 'NoHas')