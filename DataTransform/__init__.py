from DataGathering.getNameList import getNameList
from DataGathering.getVoteData import getVoteData
from DataTransform.Helpers.testTransform import testTransformContinuousVar, testTransformDiscreteVar
from DataTransform.getAverageWordSize import getAverageWordSize
from DataTransform.getLexicalDiversity import getLexicalDiversity
from DataTransform.getProperNamePresence import getProperNamePresence
from DataTransform.getSpeechSize import getSpeechSize
from DataTransform.getWordPresence import getWordPresence, addTopDifferentWordsPresence


def Test():
    votes = getVoteData()
    namesList = getNameList()

    testTransformContinuousVar(votes, 'SpeechSize', getSpeechSize)
    testTransformContinuousVar(votes, 'LexicalDiversity', getLexicalDiversity)
    testTransformContinuousVar(votes, 'AverageWordSize', getAverageWordSize)
    testTransformDiscreteVar(votes, 'WordPresence_presidente', lambda x : getWordPresence(x,'presidente'))
    testTransformDiscreteVar(votes, 'WordPresence_cunha', lambda x : getWordPresence(x,'cunha'))
    testTransformDiscreteVar(votes, 'WordPresence_dilma', lambda x : getWordPresence(x,'dilma'))
    testTransformDiscreteVar(votes, 'WordPresence_democracia', lambda x : getWordPresence(x,'democracia'))
    testTransformDiscreteVar(votes,'NamesPresence',lambda x: getProperNamePresence(x,namesList))

    addTopDifferentWordsPresence(votes)
    pass

# Test()