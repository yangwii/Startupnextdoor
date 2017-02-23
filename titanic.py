# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:02:30 2017

@author: yangpengjs
"""

import operator
import re
import pandas as pd
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

titanic = pd.read_csv('http://jizhi-10061919.file.myqcloud.com/kaggle_sklearn/titanic_train.csv')
# print titanic.head(5)
# print titanic.describe()
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 1
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 0

titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

# predictions = []
# for train, test in kf:
#     # print train, test
#     train_predictors = (titanic[predictors].iloc[train, :])
#     train_target = titanic['Survived'].iloc[train]
    
#     alg.fit(train_predictors, train_target)
    
#     test_predictions = alg.predict(titanic[predictors].iloc[test, :])
#     predictions.append(test_predictions)
    
# predictions = np.concatenate(predictions, axis=0)
# predictions[predictions > .5] = 1
# predictions[predictions <= .5] = 0

# accuracy = sum(predictions[predictions == titanic['Survived']]) / len(predictions)

# print accuracy

titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch']
titanic['NameLength'] = titanic['Name'].apply(lambda x: len(x))

def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ''
    
titles = titanic['Name'].apply(get_title)

title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}

for k, v in title_mapping.items():
    titles[titles == k] = v 
    
titanic['Title'] = titles

family_id_mapping = {}
def get_family_id(row):
    last_name = row['Name'].split(',')[0]
    family_id = '{0}{1}'.format(last_name, row['FamilySize'])
    
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 0
        else:
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
            
    return family_id_mapping[family_id]
    
family_ids = titanic.apply(get_family_id, axis=1)
family_ids[titanic['FamilySize'] < 3] = -1
titanic['FamilyId'] = family_ids

predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "FamilySize", "Title", "FamilyId"]
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

selector = SelectKBest(f_classif, k=5)
selector.fit(titanic[predictors], titanic['Survived'])
scores = -np.log10(selector.pvalues_)

# plt.bar(range(len(predictors)), scores)
# plt.xticks(range(len(predictors)), predictors, rotation='vertical')
# plt.show()

predictors = ["Pclass", "Sex", "Fare", "Title"]       
alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=8, min_samples_leaf=4)

scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic['Survived'], cv=kf)

# print scores.mean()

predictors = ["Pclass", "Sex", "Age", "Fare", "Embarked", "FamilySize", "Title", "FamilyId"]

algorithms = [
    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), predictors],
    [LogisticRegression(random_state=1), ["Pclass", "Sex", "Fare", "FamilySize", "Title", "Age", "Embarked"]]
]

titanic_test = pd.read_csv("http://jizhi-10061919.file.myqcloud.com/kaggle_sklearn/titanic_test.csv")
titles = titanic_test["Name"].apply(get_title)
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2, "Dona": 10}
for k,v in title_mapping.items():
    titles[titles == k] = v
titanic_test["Title"] = titles

titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]

family_ids = titanic_test.apply(get_family_id, axis=1)
family_ids[titanic_test["FamilySize"] < 3] = -1
titanic_test["FamilyId"] = family_ids
titanic_test['NameLength'] = titanic_test['Name'].apply(lambda x: len(x))
titanic_test['Age'] = titanic['Age'].fillna(titanic_test['Age'].median())
titanic_test['Fare'] = titanic['Fare'].fillna(titanic_test['Fare'].median())
titanic_test.loc[titanic_test['Sex'] == 'male', 'Sex'] = 1
titanic_test.loc[titanic_test['Sex'] == 'female', 'Sex'] = 0

titanic_test['Embarked'] = titanic_test['Embarked'].fillna('S')
titanic_test.loc[titanic_test['Embarked'] == 'S', 'Embarked'] = 0
titanic_test.loc[titanic_test['Embarked'] == 'C', 'Embarked'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'Q', 'Embarked'] = 2

print titanic_test.describe()
print titanic_test[predictors].head(10)

full_predictions = []
for alg, predictors in algorithms:
    alg.fit(titanic[predictors], titanic["Survived"])
    predictions = alg.predict_proba(titanic_test[predictors].astype(float))[:,1]
    full_predictions.append(predictions)
    
predictions = (full_predictions[0] * 3 + full_predictions[1]) / 4
predictions[predictions <= .5] = 0
predictions[predictions > .5] = 1
predictions = predictions.astype(int)
submission = pd.DataFrame({
             "PassengerId": titanic_test['PassengerId'], 
             "Survived": predictions})
             
submission.to_csv('kaggle.csv', index=False)