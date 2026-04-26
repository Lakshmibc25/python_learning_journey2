list =[10,20,30,10,40,20]
new_list =[]
dup =[]
for num in list:
    if num in new_list:
        if num not in dup:
            dup.append(num)
    else:
            new_list.append(num)
    print(dup)