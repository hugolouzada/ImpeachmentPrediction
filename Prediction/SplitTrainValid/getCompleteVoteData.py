from random import random

from DataGathering.getNameList import getNameList
from DataGathering.getVoteData import getVoteData
from DataTransform import getSpeechSize, getLexicalDiversity, getAverageWordSize, getProperNamePresence, addTopDifferentWordsPresence
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer


def getCompleteVoteData(addEstadoPartidoOrdem = False,addCalculatedFeatures = False, addTopDifferentWords=False):
    votes = getVoteData()
    namesList = getNameList()

    if addCalculatedFeatures:
        votes['SpeechSize'] = getSpeechSize(votes)
        votes['LexicalDiversity'] = getLexicalDiversity(votes)
        votes['AverageWordSize'] = getAverageWordSize(votes)
        votes['NamesPresence'] = getProperNamePresence(votes, namesList)

        normalizer = Normalizer(copy=False)

        normalizer.fit_transform(votes['SpeechSize'])
        normalizer.fit_transform(votes['LexicalDiversity'])
        normalizer.fit_transform(votes['AverageWordSize'])

    if addTopDifferentWords:
        addTopDifferentWordsPresence(votes)

    if addEstadoPartidoOrdem:
        for col in ['Estado','Partido']:
            votes[col+'_encoded'] = LabelEncoder().fit_transform(votes[col])

    votes.drop('Discurso', axis=1, inplace=True)
    votes.drop('Estado', axis=1, inplace=True)
    votes.drop('Partido', axis=1, inplace=True)

    if not addEstadoPartidoOrdem:
        votes.drop('Ordem', axis=1, inplace=True)

    if (not addCalculatedFeatures) and (not addTopDifferentWords) and (not addEstadoPartidoOrdem):
        votes['RandomFeature'] = votes['Vote'].map(lambda x: random())

    return votes

getCompleteVoteData()
pass