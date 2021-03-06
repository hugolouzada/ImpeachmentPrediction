from sklearn import feature_selection
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


def featureSelection(features, X_train, y_train, X_test, y_test, plotPValue=True, plotName='', alphaCutoff=0.05):
    function_rule_selection = feature_selection.f_classif

    selection_rule = feature_selection.SelectFdr(function_rule_selection, alphaCutoff)
    selection_rule.fit(X_train.values, y_train.values)

    all_pvalues = list(filter(lambda x: pd.notnull(x[0]), zip(selection_rule.pvalues_, features)))
    filtered_pvalues = list(filter(lambda x: x[0] <= alphaCutoff, all_pvalues))
    all_select_features = list(map(lambda x: x[1], filtered_pvalues))

    if (plotPValue):
        print(plotName)
        pd.DataFrame(all_pvalues).set_index(1).sort(0).plot(kind='bar', alpha=0.7, color='green')

        plt.xlabel('Features', fontsize=30);
        plt.ylabel('P-value', fontsize=30);
        plt.legend('Pvalue')

        plt.hlines(y=alpha_cutoff, xmin=0, xmax=len(features), color='red')

        plt.xticks(fontsize=12)

        plt.savefig('Temp/pvalue_' + plotName + '.png', bbox_inches='tight')

        print('Selecting %d variables from %d, (%.1f %%)' % (
        len(all_select_features), len(features), len(list(filtered_pvalues)) * 100 / float(len(features))))
        print(all_select_features)

    if len(all_select_features) == 0:
        all_select_features.append('RandomFeature')

    return X_train[all_select_features], y_train, X_test[all_select_features], y_test

    # featureSelection()
