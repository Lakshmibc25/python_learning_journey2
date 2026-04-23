num = int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print("The number is divisible by both 2 and 3.")
elif num % 2 == 0:
    print("The number is even.")
elif num%3 == 0:
    print("The number is divisible by 3.")

else:
    print("none of the above conditions are true.")