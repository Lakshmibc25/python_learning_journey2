list = [234,567,765,234,789]
new_list = []
for num in list:
    if num not in new_list:
        new_list.append(num)
print("list without duplicates:",new_list)