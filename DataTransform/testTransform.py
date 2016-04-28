import matplotlib.pyplot as plt

string_to_test = 'You say yes, I say no you say stop and I say go go go, oh no'

def testTransform(df,newVarName,transformFunction,targetVar = 'Vote'):
    df[newVarName] = transformFunction(df)

    plt.figure()
    df.boxplot(column=newVarName, by=targetVar)
    plt.savefig('Temp/'+newVarName+'by'+targetVar+'.png')
    plt.close()