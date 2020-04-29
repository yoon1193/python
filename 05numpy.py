# import numpy
# a=numpy.arrat([1,2])
# print(a,"",type(a))

# import numpy as np
# a=np.array([1,2])
# print(a)

# from numpy import exp
# result =exp()
# print (type(result," ",result))

# from numpy import array
# a=array([1,2])
# print(a)

# from numpy import *
# a=array([1,2])
# result =exp()
# print (exp(1),log(1.5),sqrt(2))

#numpy는 행렬계산하기위한 라이브러리


# a=[[1,0],[0,1]]
# b=[[1,1],[1,1]]
# c=a+b
# print(c)

# import numpy as np
# a=np.array([[1,0],[0,1]])
# b=[[1,1],[1,1]]
# c=a+b#행렬연삼됨
# print(c)
# c=a*b
# print(c)

#벡터 -1차원배열
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c)
print(a.shape) # (3,) 열이 3개
print(b.shape)
print(c.shape)
print(a.ndim) #몇 차원 배열인지

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[-1,-2,-3],[-4,-5,-6]])

print(a.shape," ",a.ndim)
print(b.shape," ",b.ndim)

c=a*b

print(c)
b=b.reshape(3,2)

print(a.shape," ",a.ndim)
print(b.shape," ",b.ndim)
print(b)

