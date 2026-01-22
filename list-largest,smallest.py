numbers = [49,78,56,89,23,56]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num>largest:
        largest = num
    if num<smallest:
        smallest = num

print("largest number:",largest)
print("smallest number:",smallest)