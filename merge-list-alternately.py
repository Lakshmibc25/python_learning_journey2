list1 = [1,2,3]
list2 = ["a","b","c"]
final_list = list1 + list2
print(final_list)

merged_list =[]

for i in range(3):
    merged_list.append(list1[i])
    merged_list.append(list2[i])
print("merged list:",merged_list)

