import numpy as np
import random as rd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import confusion_matrix



data = np.genfromtxt('angka.csv', delimiter=',')
# print(dataTrain)


#np.random.shuffle(data)

#np.savetxt('drebin_random.csv',data,delimiter=',')
np.random.seed(1)
rd.seed(1)
dataTrain = np.nan_to_num(data[0:70,:-1])
label_dataTrain = np.nan_to_num(data[0:70,-1])
dataTest = np.nan_to_num(data[70:,:-1])
label_dataTest = np.nan_to_num(data[70:,-1])


clf = RandomForestClassifier(n_estimators=70, max_depth=4)
# clf = KNeighborsClassifier()
clf.fit(dataTrain, label_dataTrain)
ans = clf.predict(dataTest)
print("Random Forest :",accuracy_score(label_dataTest,ans))

clf3 = BernoulliNB()
clf3.fit(dataTrain,label_dataTrain)
ans3 = clf3.predict(dataTest)
# aNB = accuracy_score(label_dataTest,ans3)
print("Naive Bayes :",accuracy_score(label_dataTest,ans3))

eclf = VotingClassifier(estimators=[('rf',clf),('nb',clf3)],voting='hard')
eclf.fit(dataTrain,label_dataTrain)
ans4 = eclf.predict(dataTest)

# mesinMajority[i]
# cm = confusion_matrix(label_dataTest,ans4)
print("Ensemble Majority Voting: ",accuracy_score(label_dataTest,ans4))