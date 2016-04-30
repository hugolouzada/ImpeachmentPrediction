import sklearn as sk

from Prediction.SplitTrainValid.getCompleteVoteData import getCompleteVoteData


def splitVotes():
    votes = getCompleteVoteData()
    testProp = 0.2
    voteTrain, voteTest = sk.cross_validation.train_test_split(votes, test_size=testProp, random_state=15)

    features = votes.columns - ['Nome', 'Vote']
    X_train, y_train = voteTrain[features], voteTrain['Vote']
    X_test, y_test = voteTest[features], voteTest['Vote']
    return features, X_train, y_train, X_test, y_test
