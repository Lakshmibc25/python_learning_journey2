str = input("enter your string: ")

count =0
for char in str:
    if char != " ":
        count +=1
print ("total number of characters:",count)