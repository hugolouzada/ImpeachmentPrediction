from DataGathering.getVoteData import getVoteData
from DataTransform import addTopDifferentWordsPresence
from Prediction.FeatureSelection.featureSelection import featureSelection
import sklearn as sk

votes = getVoteData()

addTopDifferentWordsPresence(votes)

testProp = 0.2
voteTrain, voteTest = sk.cross_validation.train_test_split(votes, test_size=testProp, random_state=15)

features = votes.columns - ['Nome', 'Vote', 'Estado', 'Partido','Discurso','Ordem']
X_train, y_train = voteTrain[features], voteTrain['Vote']
X_test, y_test = voteTest[features], voteTest['Vote']

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='topDifferentWords')