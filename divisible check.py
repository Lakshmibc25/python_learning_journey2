num = int(input("enter your number: "))
if num%3==0 and num%5==0:
    print("num is divisible by both 3 and 5")
elif num%3==0:
    print("num is divisible by 3 only")
elif num%5==0:
    print("num is divisible by 5 only")
else:
    print("num is not divisible by both 3 and 5")