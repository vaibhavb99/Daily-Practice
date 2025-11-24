# 9.wap to check if the given string is palindrome(take user input)

#1st way
check_str = str(input("Enter string to check if palindrome: "))

rev_str = ""

for ch in check_str:
    rev_str = ch + rev_str
    
if check_str == rev_str:
    print("The given string is palindrome.")
else:
    print("Not Palindrome.")
    
    
#2nd way

check_str = str(input("Enter string to check if palindrome: "))

rev_str = "".join(reversed(check_str))

if check_str == rev_str:
    print("The given string is palindrome.")
else:
    print("Not Palindrome.")


#3rd way

check_str = str(input("Enter string to check if palindrome: "))

rev_str = check_str[::-1]

if check_str == rev_str:
    print("The given string is palindrome.")
else:
    print("Not Palindrome.")