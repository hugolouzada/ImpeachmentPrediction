from time import time
import sklearn as sk


def getEstimation(classifier, X_train, y_train, X_test, y_test, verbose=True):

    start = time()
    classifier.fit(X_train, y_train.values)

    if verbose:
        print('Estimation time: %ds' % (time() - start))

    predictedTest = classifier.predict(X_test)

    aucScore = sk.metrics.roc_auc_score(y_test, predictedTest)

    if verbose:
        print(classifier.get_params())
        print(aucScore)

    return aucScore

# getEstimation()