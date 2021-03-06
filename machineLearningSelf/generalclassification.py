from sklearn import tree,metrics

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# decision tree classifier

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

validate = [[189, 65, 48]]
prediction = clf.predict(validate)
print(prediction)
print(metrics.accuracy_score(['male'], prediction))


## Nearest Neighbour

from sklearn.neighbors import KNeighborsClassifier

clf1 = KNeighborsClassifier()
clf1 = clf1.fit(X, Y)
prediction1 = clf1.predict(validate)
print(prediction1)
print(metrics.accuracy_score(['male'], prediction1))

