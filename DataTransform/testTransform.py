import matplotlib.pyplot as plt

def testTransform(df,varName,transformFunction,targetVar = 'Vote'):
    df[varName] = transformFunction(df)

    plt.figure()
    df.boxplot(column=varName, by=targetVar)
    plt.savefig('Temp/'+varName+'by'+targetVar+'.png')