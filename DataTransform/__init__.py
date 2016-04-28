from DataGathering.getVoteData import getVoteData
from DataTransform.Helpers.testTransform import testTransformContinuousVar, testTransformDiscreteVar
from DataTransform.getAverageWordSize import getAverageWordSize
from DataTransform.getLexicalDiversity import getLexicalDiversity
from DataTransform.getSpeechSize import getSpeechSize
from DataTransform.getWordPresence import getWordPresence

votes = getVoteData()

testTransformContinuousVar(votes, 'SpeechSize', getSpeechSize)
testTransformContinuousVar(votes, 'LexicalDiversity', getLexicalDiversity)
testTransformContinuousVar(votes, 'AverageWordSize', getAverageWordSize)
testTransformDiscreteVar(votes, 'WordPresence_presidente', lambda x : getWordPresence(x,'presidente'))
testTransformDiscreteVar(votes, 'WordPresence_cunha', lambda x : getWordPresence(x,'cunha'))
