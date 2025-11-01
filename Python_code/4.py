#4.wap to check if the given string has even length of character.

user_input = str(input("Enter your string: "))
if len(user_input) % 2 == 0:
    print("Even length string.")
else:
    print("Odd length string.")
