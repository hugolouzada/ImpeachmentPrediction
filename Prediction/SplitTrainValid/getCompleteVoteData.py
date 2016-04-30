from DataGathering.getNameList import getNameList
from DataGathering.getVoteData import getVoteData
from DataTransform import getSpeechSize, getLexicalDiversity, getAverageWordSize, getProperNamePresence


def getCompleteVoteData():
    votes = getVoteData()
    namesList = getNameList()

    votes['SpeechSize'] = getSpeechSize(votes)
    votes['LexicalDiversity'] = getLexicalDiversity(votes)
    votes['AverageWordSize'] = getAverageWordSize(votes)
    votes['NamesPresence'] = getProperNamePresence(votes, namesList)

    votes.drop('Discurso', axis=1, inplace=True)

    return votes
