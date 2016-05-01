from DataGathering.getNameList import getNameList
from DataGathering.getVoteData import getVoteData
from DataTransform import getSpeechSize, getLexicalDiversity, getAverageWordSize, getProperNamePresence
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer


def getCompleteVoteData():
    votes = getVoteData()
    namesList = getNameList()

    votes['SpeechSize'] = getSpeechSize(votes)
    votes['LexicalDiversity'] = getLexicalDiversity(votes)
    votes['AverageWordSize'] = getAverageWordSize(votes)
    votes['NamesPresence'] = getProperNamePresence(votes, namesList)


    for col in ['Estado','Partido']:
        votes[col+'_encoded'] = LabelEncoder().fit_transform(votes[col])

    votes.drop('Discurso', axis=1, inplace=True)
    # votes.drop('Estado', axis=1, inplace=True)
    # votes.drop('Partido', axis=1, inplace=True)

    normalizer = Normalizer(copy=False)

    normalizer.fit_transform(votes['SpeechSize'])
    normalizer.fit_transform(votes['LexicalDiversity'])
    normalizer.fit_transform(votes['AverageWordSize'])

    return votes

# getCompleteVoteData()