# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:28:50 2017

@author: yangpengjs
"""

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn import decomposition

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

pca = decomposition.PCA()
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, random_state=1)
pipe = Pipeline(steps=[('pca', pca), ('nn', mlp)])

pipe.fit(train.iloc[:, 1:], train['label'])
joblib.dump(mlp, 'mlp.model')
target = pipe.predict(test)

submission = pd.DataFrame({
             'ImageId': [x for x in range(1, test.shape[0] + 1)],
             'Label': target})
submission.to_csv('kaggle.csv', index=False)