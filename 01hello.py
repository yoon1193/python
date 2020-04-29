print("hello world")
print("hi Yoon")
#주석
#세미콜론 없어도됨,배열없음,변수선언x
#data type
#list(배열같은) tuple dictionary string

#list
a=[10,20,30,40,50]#배열x , list o
print("a[0]=",a[0],"a[1]=",a[1])
print("a[0]=",a[-1],"a[1]=",a[-2])

b=[10,20,"hello",[True,3.24]]
print("b[2]=",b[2],"b[3]=",b[3][0])
print("b[2]=",b[2],"b[3]=",b[-1][-2])#같은결과

c=[]
c.append(100),c.append(200),c.append(300)
print(c[0:2])#0인덱스부터 2인덱스 이전까지
print(c[1:3])
print(a[:])
print(a[:3])
print(a[:-2])
a[1]=50
print(a)

#tuple=list와 비슷한데 상수처럼 변경 불가
a=(10,20,30,40,50) #()
#a[0]=4 변경이불가

#dictionary
#키(key)와 값(values)으로 data가 쌍으로 존재
score={"kim":90,"lee":29,"jun":99}
print(score)
print(score["kim"])
print(score.keys())
print(score.values())
print(score.items())
score["kim"]=44
print(score["kim"])

#string
a='a24,sa'
#a=[1] '2'라는 문자열을 리턴
print(a[1])
a=a+',asdfasdf'
print(a)
b=a.split(',')
print(b)

#함수
a=[10,20,30,40,50]
b=[10,20,30,40,50]
c={"kim":90,"lee":29,"jun":99}
d="hello world"
e=[[100,200],[300,400],[500,600]]


#type=datatype을 알려줌
print(type(a),type(b),type(c),type(d),type(e))

#len=data 길이 리턴
#size=원소의 개수 리턴
print(len(a),len(b),len(c),len(d),len(e))


a='hello'
print(list(a))#list로 바꿈
print(str('3.14'))
print(str([1,2,3]))

print(int(3.14))
print(int('3'))
print(float('3.14'))
