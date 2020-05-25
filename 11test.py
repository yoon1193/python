from sklearn import svm,metrics
clf = svm.SVC() #인공지능객체를 변수에

# clf.fit(입력데이터,출력데이터) 데이터셋팅 (학습)
# 질문의 답 = clf.predict(질문데이터) (질문)
# print(질문의 답)

clf = svm.SVC()
clf.fit([[0,0],[0,1],[1,0],[1,1]],[0,1,1,1])
result = clf.predict([[0,0],[1,0]])
print(result)
score = metrics.accuracy_score([0,1],result) #1.0 = 100%
print(score)
