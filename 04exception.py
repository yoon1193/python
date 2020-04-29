def calc(data):
    sum=0
    try:
        sum=data[0]+data[1]+data[2]
        if sum<0:
            raise Exception("sum error")
    except IndexError as err:
        print(str(err))
    except Exception as err:
        print(str(err))
    finally:
        print(sum)
calc([1,2,3])
calc([-1,-2,-3])

f=open("파일명","w")
f.write("asdf")
f.close()
#with 알아서 닫아줌 (java using)
with open("파일명") as f:
    f.write("asdf")