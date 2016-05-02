import random
import sklearn.linear_model as sklin
import sklearn.neighbors as skneib
import sklearn.ensemble as skes
import sklearn.tree as sktr

import pickle

from Prediction.ModelEstimation.getEstimationForMultipleFeatureSets import getEstimationForMultipleFeatureSets

randomSeed = 15

random.seed(randomSeed)

classifiers = [skes.RandomForestClassifier(),sktr.DecisionTreeClassifier(),skes.GradientBoostingClassifier(),sklin.RidgeClassifier(),skneib.KNeighborsClassifier()] #skes.RandomForestClassifier(n_estimators=int(random()*10+1))

tries=0
while True:

    classifier = random.choice(classifiers)
    classifierParameter = 0
    if isinstance(classifier,skes.RandomForestClassifier) or isinstance(classifier,sktr.DecisionTreeClassifier)  or isinstance(classifier,skes.GradientBoostingClassifier) :
        classifier.min_samples_leaf = random.randint(10,100)
        classifierParameter = classifier.min_samples_leaf
    if isinstance(classifier, sklin.RidgeClassifier):
        classifier.alpha = random.random()
        classifierParameter = classifier.alpha
    if isinstance(classifier, skneib.KNeighborsClassifier):
        classifier.leaf_size = random.randint(10,100)
        classifierParameter = classifier.leaf_size

    alphaCutoff = 0.10*random.random()

    try:
        featureSet = getEstimationForMultipleFeatureSets(classifier,alphaCutoff,randomSeed=randomSeed,verbose=False)

        result = [classifier,[alphaCutoff,classifierParameter],featureSet]
        print(tries, result)

        with open("Temp/multipleModels_performance.p","ab") as file:
            pickle._dump(result,file)
        tries += 1

    except:
        print("Error on something!")



