import numpy as np



#미분
# def myFun1(x):
#     return x**2 #x제곱
# def numeric_derivative(f,x):
#     myZero = 1e-4 #프로그램상 0에 가까운
#     return (f(x+myZero)-f(x-myZero))/2*myZero 
# result = numeric_derivative(myFun1,2)
# print(result)

# 편미분
# f(x,y)=2x+3xy+y^3
def myFun2(data):
    x = data[0]
    y = data[1]
    return 2*x+3*x*y+np.power(y,3)
def numeric_upgrade(f,x):
    myZero = 1e-4 
    grad = np.zeros_like(x)
    it = np.nditer(x,flags=['multi_index'],op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp = x
        tmp[0] = tmp[0]+myZero
        fun1 = f(tmp)

        tmp = x
        tmp[0] = tmp[0]-myZero
        fun2 = f(tmp)

        grad[idx] = (fun1 - fun2)/2*myZero
    
        it.iternext()
    return grad 
result = numeric_upgrade(myFun2,[2,2])
print(result)