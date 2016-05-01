from time import time
import sklearn.ensemble as skes
import sklearn as sk


from Prediction.FeatureSelection.featureSelection import featureSelection


def getEstimation(verbose=True):

    X_train, y_train, X_test, y_test = featureSelection(plotPValue = False)

    start = time()
    rf = skes.RandomForestClassifier(n_estimators=5)
    rf.fit(X_train, y_train.values)

    if verbose:
        print('Estimation time: %ds' % (time() - start))

    predictedTest = rf.predict(X_test)

    aucScore = sk.metrics.roc_auc_score(y_test, predictedTest)

    if verbose:
        print(rf.get_params())
        print(aucScore)

    return aucScore

# getEstimation()