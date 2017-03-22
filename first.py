from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
#decision tree classifier
clf = tree.DecisionTreeClassifier()
#fit is used to find  patterns in data.
clf=clf.fit(features,labels)
print  (clf.predict([[150,0]]))