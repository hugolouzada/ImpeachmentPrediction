from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

string_to_test = 'You say yes, I say no you say stop and I say go go go, oh no'


def testTransformContinuousVar(df, newVarName, transformFunction, targetVar='Vote'):
    df[newVarName] = transformFunction(df)

    plt.figure()
    df.boxplot(column=newVarName, by=targetVar)
    plt.savefig('Temp/' + newVarName + 'by' + targetVar + '.png')
    plt.close()

def testTransformDiscreteVar(df, newVarName, transformFunction, targetVar='Vote'):
    df[newVarName] = transformFunction(df)

    plt.figure()
    mosaic(df, [targetVar, newVarName])
    plt.savefig('Temp/' + newVarName + 'by' + targetVar + '.png')
    plt.close()