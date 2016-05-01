from Prediction.FeatureSelection.featureSelection import featureSelection
from Prediction.SplitTrainValid.splitVotes import splitVotes

features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem = False, addCalculatedFeatures=False, addTopDifferentWords=True)

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='TopDifferentWords')

features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem = False, addCalculatedFeatures=True, addTopDifferentWords=False)

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='CalculatedFeatures')

features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem = True, addCalculatedFeatures=False, addTopDifferentWords=False)

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='EstadoPartidoOrdem')

features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem = True, addCalculatedFeatures=True, addTopDifferentWords=False)

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='EstadoPartidoOrdem_Calculated')

features, X_train, y_train, X_test, y_test = splitVotes(addEstadoPartidoOrdem = True, addCalculatedFeatures=True, addTopDifferentWords=True)

featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True,plotName='All')

