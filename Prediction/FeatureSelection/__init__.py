import sklearn as sk
from sklearn import feature_selection
import pandas as pd
import matplotlib.pyplot as plt

from Prediction.SplitTrainValid.splitVotes import splitVotes

function_rule_selection = feature_selection.f_classif
alpha_cutoff = 0.01

features, X_train, y_train, X_test, y_test = splitVotes()

selection_rule = feature_selection.SelectFdr(function_rule_selection, alpha_cutoff)
selection_rule.fit(X_train.values, y_train.values)


all_pvalues = list(filter(lambda x: pd.notnull(x[0]), zip(selection_rule.pvalues_, features)))
filtered_pvalues = list(filter(lambda x: x[0]<=alpha_cutoff, all_pvalues))
all_select_features = list(map(lambda x: x[1], filtered_pvalues))

print('Were selected %d variables from %d, (%.1f %%)' % (len(all_select_features), len(features), len(list(filtered_pvalues)) * 100 / float(len(features))))

pd.DataFrame(all_pvalues).set_index(1).sort(0).plot(kind='bar', alpha=0.7, color='green')

plt.xlabel('Features', fontsize=30); plt.ylabel('P-value', fontsize=30); plt.legend('Pvalue')

plt.hlines(y=0.01, xmin=0, xmax=len(features), color='red')

plt.xticks(fontsize=12)

plt.savefig('Temp/pvalue_someFeatures.png',bbox_inches='tight')