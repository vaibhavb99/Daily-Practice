#6.wap to check if the given programming language is present in the list.
# p = ["java", "python","c","c++","Ruby","Golang"]

p = ["java", "python","c","c++","ruby","golang"]

user_input = str(input("Enter programming language name: ")).lower()

if user_input in p:
    print(f"yes the {user_input} language is available.")
else:
    print(f"Sorry, {user_input} is not available.")