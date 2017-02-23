
from sklearn import datasets
from sklearn.lda import LDA

iris = datasets.load_iris()
X = iris[:-5]
pre_x = iris[-5:]
y = iris.target[:-5]

print 'raw sample:'
print X[:10]

clf = LDA()
clf.fit(X, y)
x_r = clf.transform(X)
pre_y = clf.predict(pre_x)

print 'transformed sample:'
print x_r[:10]

print 'target:'
print pre_y