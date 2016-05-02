from Prediction.FeatureSelection.featureSelection import featureSelection
from Prediction.FeatureSelection.getFeatureSetName import getFeatureSetName
from Prediction.ModelEstimation.getEstimation import getEstimation
from Prediction.SplitTrainValid.splitVotes import splitVotes


def getEstimationForMultipleFeatureSets(classifier, alphaCutoff, verbose=True, randomSeed=15):
    featureSets = {}

    for addEstadoPartidoOrdem in [True, False]:
        for addCalculatedFeatures in [True, False]:
            for addTopDifferentWords in [True, False]:

                if verbose:
                    print(getFeatureSetName(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords))

                features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords, randomSeed)

                X_train_features, y_train, X_test_features, y_test = featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=False,alphaCutoff=alphaCutoff)

                featureSets[getFeatureSetName(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords)] = getEstimation(classifier, X_train_features, y_train, X_test_features, y_test, verbose=verbose)

    return featureSets