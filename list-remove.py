list=["lakshmi","banana","","orange","apple",""]
final_list = []

for word in list:
    if word != "":
        final_list.append(word)

print("list after removing empty string:",final_list)
