def sum(x,y):
    s=x+y
    return s
result=sum(10,20)
print(result)


def mutiFunc(x):
    return x+1,x+2,x+3
x1,x2,x3=mutiFunc(1)
print(x1,x2,x3)

#람다식
#함수를 만들어서 실행
f=lambda x: x+100
for i in range(3):
    print(f(i))

def print_hello():
    print('hello')
def test_lambda(s,t):
    print(s,t)
test_lambda(1,2)
fx=lambda x,y:test_lambda(x,y)
fy=lambda x,y:print_hello()
fx(500,100)
fy(2,1)
