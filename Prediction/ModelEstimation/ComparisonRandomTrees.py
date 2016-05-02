import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.linear_model as sklin
import sklearn.ensemble as skes
import sklearn.tree as sktr
import sklearn.neighbors as skneib
from numpy import average, std
from pandas import DataFrame

from Prediction.FeatureSelection.getFeatureSetName import getFeatureSetName
from Prediction.FeatureSelection.featureSelection import featureSelection
from Prediction.ModelEstimation.getEstimation import getEstimation
from Prediction.SplitTrainValid.splitVotes import splitVotes

# classifier = skes.RandomForestClassifier(n_estimators=5)
# classifier = sktr.DecisionTreeClassifier()
# classifier = skes.GradientBoostingClassifier()
# classifier = sklin.RidgeClassifier()
classifier = skneib.KNeighborsClassifier()
classifierName = "KNeighborsClassifier"

tries = 3
featureSets = {}

for addEstadoPartidoOrdem in [True, False]:
    for addCalculatedFeatures in [True, False]:
        for addTopDifferentWords in [True, False]:

            scores = []
            print(str([addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords]))
            for randomSeed in range(0, tries):
                features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem, addCalculatedFeatures,
                                                                        addTopDifferentWords, randomSeed)

                X_train_features, y_train, X_test_features, y_test = featureSelection(features, X_train, y_train,
                                                                                      X_test, y_test, plotPValue=False)

                scores.append(
                    getEstimation(classifier, X_train_features, y_train, X_test_features, y_test, verbose=False))

            featureSets[getFeatureSetName(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords)] = scores
            print(average(scores), std(scores))

sns.set(style="whitegrid", color_codes=True)
ax = sns.boxplot(data=DataFrame(featureSets), palette="Set2")

plt.xticks(rotation='vertical')
plt.savefig("Temp/roc_"+classifierName+"_tries"+str(tries)+".png", bbox_inches='tight')
