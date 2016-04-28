from DataTransform.sanitizeString import sanitizeString

def getSpeechSize(df):
    return df['Discurso'].map(lambda d: len(sanitizeString(str(d))))


