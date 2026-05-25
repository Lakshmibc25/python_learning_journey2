dict = {
    "name":"lakshmi",
    "age":20
}
print(dict)

dict.update({"course":"python"})
print(dict)

print(dict.keys())

dict.update({"age":21})
print(dict)

print(dict.values())

if "name" in dict:
   print("key is there in dict")
else:
    print("key is not there in dict")
