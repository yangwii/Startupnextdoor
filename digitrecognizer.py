# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:16:39 2017

@author: yangpengjs
"""

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# print train.head(5)
# print train.shape[0]

# train.iloc[:, 1:] get data
# mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, random_state=1)
# mlp.fit(train.iloc[:, 1:], train['label'])
# joblib.dump(mlp, 'mlp.model')
mlp = joblib.load('mlp.model')
score = cross_val_score(mlp, train.iloc[:, 1:], train['label'], cv = 5)
print score.mean()

target = mlp.predict(test)
# joblib.dump(mlp, 'mlp.model')
# print train['label'][30000:]
submission = pd.DataFrame({
             'ImageId': [x for x in range(1, test.shape[0] + 1)],
             'Label': target})
submission.to_csv('kaggle.csv', index=False)