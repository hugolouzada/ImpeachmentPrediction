def getSpeechSize(df):
    return df['Discurso'].map(lambda d: len(str(d)))
