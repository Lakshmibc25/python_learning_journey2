str = input("enter your string: ")
vowel = "a","e","i","o","u"

count = 0
for ch in str:
    if ch.lower() in vowel:
      count+=1
print(count)
