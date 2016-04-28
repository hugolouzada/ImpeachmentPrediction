def calculateLexicalDiversity(text):
    textSplit = text.split()

    return len(set(textSplit))/len(textSplit)

def getLexicalDiversity(df):
    return df['Discurso'].map(lambda d: calculateLexicalDiversity(str(d)))

print(len('You say yes, I say no you say stop and I say go go go, oh no'.split()))
print((set('You say yes, I say no You say stop and I say go go go, oh no'.split())))
print(calculateLexicalDiversity('You say yes, I say no You say stop and I say go go go, oh no'))
