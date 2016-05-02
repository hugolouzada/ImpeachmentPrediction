import seaborn as sns
from pandas import DataFrame

import matplotlib.pyplot as plt

import pickle

file = open("Temp/multipleModels_performance.p","rb")

bestModels = {}

tries= 0

while 1:
    try:
        result = pickle.load(file)
        print("model ",tries)
        for pair in result[2].items():
            if pair[0] in bestModels:
                if pair[1]> bestModels[pair[0]][0]:
                    bestModels[pair[0]][0] = pair[1]
                    bestModels[pair[0]][1] = [result[0],result[1]]
            else:
                bestModels[pair[0]] = [pair[1], [result[0], result[1]]]
        tries+=1

    except EOFError:
        break

    except KeyError:
        pass

dataToPlot = {}
for pair in bestModels.items():
    dataToPlot[pair[0]] = [pair[1][0]]
    print(pair)

sns.set(style="whitegrid", color_codes=True)
ax = sns.boxplot(data=DataFrame(dataToPlot), palette="Set2")

plt.xticks(rotation='vertical')
plt.savefig("Temp/roc_multipleModels.png", bbox_inches='tight')