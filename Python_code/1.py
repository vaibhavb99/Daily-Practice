try:
    user_input = eval(input("Enter a number to check if it is odd or even: "))
    if user_input%2==0:
        print("even number")
    elif user_input%2==1:
        print("odd number")
    else:
        print("Invalid input")
except Exception as e:
    print("Input is not a number !")