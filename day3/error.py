# arthematic error 
try:
    num = int(input("enter a number"))
    print(10/num)
except ZeroDivisionError:
    print("can not be devisbale")
except  ValueError:
    print("enter only numer")
finally:
    print("thank you for responce")   