try:
    num = int(input("enter a number :"))
    result = 10/num
    print("result:" , result)
except ZeroDivisionError:
    print("cannot divide by zero.")
except ValueError:
    print("please enter a valid number.")