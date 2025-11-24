# 8.wap to check if the given number is positive. Take user input.

check_num = float(input("Enter number to check: "))

if(check_num > 0):
    print(f"The number {check_num} is positive.")
elif(check_num < 0):
    print(f"The number {check_num} is negative.")
else:
    print("0 is not +ve or -ve.")