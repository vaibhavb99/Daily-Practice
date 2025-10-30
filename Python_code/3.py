#3.wap to check which number is greater using if condition.
try:
    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number: "))

    if a>b:
        print(a, " is greater !")
    elif b>a:
        print(b, " is greater !")
    elif a==b:
        print("both numbers are same !")
    else:
        print("Invalid input !")
except Exception as e:
    print("not a number ! can not be compared.")