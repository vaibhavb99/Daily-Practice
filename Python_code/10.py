# 10.wap to check if the first letter in the given string is consonant.

check_consonant = str(input("Enter String: "))

if(check_consonant[0] not in "aeiou"):
    print("Consonant.")
else:
    print("Vowel")