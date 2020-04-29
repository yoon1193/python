import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([[-1,-2,-3],[-4,-5,-6]])
# b=b.reshape(3,2)
# # c=a*b
# c=np.dot(a,b)
# print(c)

#broadcase 알아서 값을 채워서 행렬계산을 실행
a=np.array([[1,2,3],[4,5,6]])
c=a+5
print(c)
d=[1,2,3]
c=a+d
print(c)
c=c.T #전치행렬
print(c)