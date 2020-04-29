class Person:
    count=0#class변수
    def __init__(self,name):
        Person.count+=1
        self.name=name#인스턴스변수
        print(self.name+"초기화 함수")

    def work(self,company):
        print(self.name+"회사"+company)

    def sleep(self):
        print(Person.count)
        print(self.name)
        self.__myName()#class 안 함수호출
        myName()#class 밖 함수호출

    def __myName(self):#__ 밑줄2개 private함수
        print('hello')

    @classmethod
    def getCount(cls):
        return cls.count
        
def myName():#class 밖 함수
    print('hi')

obj = Person("park")
obj.work("abc")
obj.sleep()
print(Person.getCount())