from DataGathering.sanitizeString import sanitizeString

def getSpeechSize(df):
    return df['Discurso'].map(lambda d: float(len(sanitizeString(str(d)))))


