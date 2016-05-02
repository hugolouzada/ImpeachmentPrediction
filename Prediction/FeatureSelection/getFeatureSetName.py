def getFeatureSetName(addEstadoPartidoOrdem, addCalculatedFeatures, addTopDifferentWords):
    name = ""
    if addEstadoPartidoOrdem:
        name = "Political"
    if addCalculatedFeatures:
        name += "_MetaSpeech"
    if addTopDifferentWords:
        name += "_Words"
    return "None" if name == "" else name