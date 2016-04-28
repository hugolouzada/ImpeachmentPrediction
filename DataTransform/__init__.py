
#palavras mais usadas

#presidente implica vota sim



from DataTransform.testTransform import testTransform
from DataTransform.getSpeechSize import getSpeechSize
from DataGathering.getVoteData import getVoteData

votes = getVoteData()

testTransform(votes,'Discurso',getSpeechSize)
