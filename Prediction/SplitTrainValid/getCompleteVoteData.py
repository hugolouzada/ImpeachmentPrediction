from random import random

from DataGathering.getNameList import getNameList
from DataGathering.getVoteData import getVoteData
from DataTransform import getSpeechSize, getLexicalDiversity, getAverageWordSize, getProperNamePresence, addTopDifferentWordsPresence
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.feature_extraction import DictVectorizer
import pandas as pd



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
        categoricalValues = votes[['Estado','Partido']]
        categoricalDict = categoricalValues.T.to_dict().values()
        vec = DictVectorizer()
        multiCategory = pd.DataFrame(vec.fit_transform(categoricalDict).toarray())
        multiCategory.columns = vec.get_feature_names()
        votes = pd.concat([votes, multiCategory], axis=1)


    votes.drop('Discurso', axis=1, inplace=True)
    votes.drop('Estado', axis=1, inplace=True)
    votes.drop('Partido', axis=1, inplace=True)

    if not addEstadoPartidoOrdem:
        votes.drop('Ordem', axis=1, inplace=True)

    if (not addCalculatedFeatures) and (not addTopDifferentWords) and (not addEstadoPartidoOrdem):
        votes['RandomFeature'] = votes['Vote'].map(lambda x: random())

    return votes

# getCompleteVoteData(addEstadoPartidoOrdem=True)
