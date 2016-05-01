from Prediction.FeatureSelection.featureSelection import featureSelection
from Prediction.SplitTrainValid.splitVotes import splitVotes


def getFeatures(addEstadoPartidoOrdem = False,addCalculatedFeatures = False, addTopDifferentWords=False):
    features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords)
    return featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=False)