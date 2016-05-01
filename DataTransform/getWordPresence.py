from Analysis.topDifferentWords import topDifferentWords
from DataGathering.sanitizeString import sanitizeString


def getWordPresence(df,word):
    return df['Discurso'].map(lambda d: word in sanitizeString(str(d)))


def addTopDifferentWordsPresence(df):

    topDif = topDifferentWords(df)

    for word in topDif.topWords('Yes',plotWordCloud=False)+topDif.topWords('No',plotWordCloud=False):
        df["Has_"+word]  =getWordPresence(df,word)

