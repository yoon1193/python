import pandas
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
# Iris-setosa 0
# Iris-versicolor 1
# Iris-virginica 2
# SepalLength,SepalWidth,PetalLength,PetalWidth,Name
csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]
# 학습시킬 데이터를 train_data
# 테스트할 데이터를 test_data
train_data,test_data,train_label,test_label = train_test_split(data,label)
print(train_data)
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label,pre)
print(ac_score)

# print(data)
# print(label)

# clf = svm.SVC()
# clf.fit(data,label)
# result = clf.predict([[4.8,3.4,1.6,0.2,0],[4.8,3.4,1.5,0.2,0],[4.8,3.1,1.6,0.2,0]])
# print(result)