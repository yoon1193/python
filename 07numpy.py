import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3)
print(a.shape)
print(a)
print(a[0][0],a[0,0]) # [행,열]
print(a[0][1],a[0,1])
print(a[2][1],a[3,2]) 

print(a[0:-1,1:2])
print(a[:,0])

# a를 순서대로 찍기 iterator 생성
it = np.nditer(a,flags=['multi_index'],op_flags=['readwrite'])
while not it.finished:
    idx = it.multi_index
    print(a[idx])
    it.iternext()
    

# concatenate
a = np.array([[10,20,30],[40,50,60]])
print(a)
b = np.array([70,80,90]).reshape(1,3)
a1 = np.concatenate((a,b),axis=0) #axis 0이면 행에추가 1이면 열에추가
print(a1)
a2 = np.concatenate((a1,b.reshape(3,1)),axis=1)
print(a2)


load_data = np.loadtxt('./data.csv',delimiter=',',dtype=np.float32)
print(load_data)
x_data = load_data[:,0:-1]
y_data = load_data[:,-1]
print(x_data,x_data.ndim,x_data.shape)
print(y_data,y_data.ndim,y_data.shape)

r1 = np.random.rand(3)
r2 = np.random.rand(1,3)
r3 = np.random.rand(3,1)
print(r1,r1.shape)
print(r2,r2.shape)
print(r3,r3.shape)

x = np.array([2,4,6,8])
print(np.sum(x))
print(np.exp(x)) #지수  e
print(np.log(x))
print(np.max(x))
print(np.min(x))
print(np.argmax(x)) #가장큰값 인덱스 리턴
print(np.argmin(x))

a = np.ones([3,3]) #1로 채워진 행렬생성
b = np.zeros([2,4]) #0으로
print(a)
print(b)

x = np.array([[2,4,6],[1,2,3],[0,5,8]])
print(np.max(x,axis=1))
print(np.min(x,axis=1))
print(np.argmax(x,axis=1))
print(np.argmin(x,axis=1))