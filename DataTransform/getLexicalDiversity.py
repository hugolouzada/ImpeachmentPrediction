from DataTransform.Helpers.sanitizeString import sanitizeString

def calculateLexicalDiversity(text):
    textSplit = sanitizeString(text).split()

    return len(set(textSplit))/len(textSplit)

def getLexicalDiversity(df):
    return df['Discurso'].map(lambda d: calculateLexicalDiversity(str(d)))

# txt = string_to_test
# txt = sanitizeString(txt)
# print(txt)
# print((txt.split()))
# print((set(txt.split())))
# print(len(set(txt.split()))/len(txt.split()))
# print(calculateLexicalDiversity(txt))
