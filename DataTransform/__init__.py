from DataTransform.getAverageWordSize import getAverageWordSize
from DataTransform.testTransform import testTransform
from DataTransform.getSpeechSize import getSpeechSize
from DataTransform.getLexicalDiversity import getLexicalDiversity
from DataGathering.getVoteData import getVoteData

votes = getVoteData()

testTransform(votes,'SpeechSize',getSpeechSize)
testTransform(votes,'LexicalDiversity',getLexicalDiversity)
testTransform(votes,'AverageWordSize',getAverageWordSize)
