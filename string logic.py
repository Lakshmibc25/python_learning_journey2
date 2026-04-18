str = input("enter your string: ")
vowels = 0
consonants = 0
for char in str:
        if char  in "aeiou":
           vowels+=1
        else:
            consonants+=1
print("vowels are:",vowels)
print("consonants are:",consonants)           