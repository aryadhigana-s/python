import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

from sklearn.ensemble import VotingClassifier

from sklearn import model_selection
#from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import tree

from sklearn.naive_bayes import BernoulliNB

# start_time = time.time()
data = np.genfromtxt('angka.csv', delimiter=',')
# print(dataTrain)


#np.random.shuffle(data)

#np.savetxt('drebin_random.csv',data,delimiter=',')
np.random.seed(1)
# rd.seed(1)
# dataTrain = np.nan_to_num(data[0:10000,:215])
# label_dataTrain = np.nan_to_num(data[0:10000,-1])
# dataTest = np.nan_to_num(data[10001:,:215])
# label_dataTest = np.nan_to_num(data[10001:,-1])

features = np.nan_to_num(data[0:,:-1])
labels = np.nan_to_num(data[0:,-1])

skf = StratifiedKFold(n_splits=5)

clf = RandomForestClassifier(n_estimators=100, max_depth=10)
# clf2 = KNeighborsClassifier(n_neighbors=5)
# clf3 = BernoulliNB()
# eclf = VotingClassifier(estimators=[('rf',clf),('knn',clf2),('nb',clf3)],voting='hard')


fold = 1
for train_index, test_index in skf.split(features, labels):
    x_train, x_test = features[train_index], features[test_index]
    y_train, y_test = labels[train_index], labels[test_index]
    print("fold {}".format(fold), end="\t")
    print("banyak data latih {}".format(len(y_train)), end="\t")
    print("banyak data uji {}".format(len(y_test)), end="\t")
    print("")
    clf.fit(x_train, y_train)
    ans = clf.predict(x_test)
    print("nilai presisi",precision_score(ans, y_test, average='micro'))
    print("nilai recall", recall_score(ans, y_test, average='micro'))
    print("akurasi {}".format(clf.score(x_test,y_test)), end="\t")
    print("")
    print("============================================")
    fold += 1