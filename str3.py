string = input("enter your string: ")
vowels = "aeiouAEIOU"

count = 0
for char in string:
    if char in vowels:
      count += 1
print("number of vowels: ", count)