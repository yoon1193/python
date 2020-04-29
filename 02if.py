a=1 
if a > 0:
    print("1.a ==",a) #tab도 하나의 문장 {}없음.
elif a==0:
    print("2.a ==",a)
else:
    print("3.a ==",a)
    print("if문 끝부분")
print("end")

a=[10,20,30,40,50]
b=[10,20,30,40,50]
c={"kim":90,"lee":29,"jun":99}
if 45 in a:#a리스트에 45가 있냐 없냐
    print("is 45")
else:
    print("is not 45")

if 'kim' in c:
    print("yes")
else:
    print("no")

for data in range(10):#for(int i=0;i<10;i++)
    print(data)
for data in range(0,10,2):#for(int i=0;i<10;i+=2)
    print(data)
for data in a:
    print(data)
for data in c:
    print(data," ",c[data])
for data,value in c.items():
    print(data," ",value)

a=[x**2 for x in range(5)]# **숫자 (숫자)제곱
print(a)
a=[[100,200],[300,400],[500,600]]
a=[x for x in a]
print(a)
a=[x*2 for x in a]
print(a)
a=[x[0] for x in a]
print(a)


#10 이하 짝수를 list
a=[]
for a in range(10):
    if a%2==0:
        print(a)
print()

a=5
while a>=0:
    print(a)
    a=a-1
    
print("end")
