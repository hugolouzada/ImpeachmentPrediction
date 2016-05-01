import sklearn.ensemble as skes
from numpy import average, std

from Prediction.FeatureSelection.featureSelection import featureSelection
from Prediction.ModelEstimation.getEstimation import getEstimation
from Prediction.SplitTrainValid.splitVotes import splitVotes

classifier = skes.RandomForestClassifier(n_estimators=5)

tries = 1000
featureSets = {}

for addEstadoPartidoOrdem in [True,False]:
    for addCalculatedFeatures in [True,False]:
        for addTopDifferentWords in [True,False]:

            scores = []
            for randomSeed in range(0,tries):
                features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords,randomSeed)

                X_train_features, y_train, X_test_features, y_test = featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=False)

                scores.append(getEstimation(classifier, X_train_features, y_train, X_test_features, y_test, verbose=False))

            featureSets[str([addEstadoPartidoOrdem,addCalculatedFeatures,addTopDifferentWords])] = scores
            print(str([addEstadoPartidoOrdem,addCalculatedFeatures,addTopDifferentWords]), average(scores),std(scores))