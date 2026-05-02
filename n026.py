list = ["mango"," ","orange"," ","apple"]
#while " " in list:
  #  list.remove(" ")
#print(list)
for char in list:
    if char == " ":
        list.remove(" ")
print(list)