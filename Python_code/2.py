try:
    score = eval(input("Enter your percentage: "))
    if score >=70:
        print("good luck !")
    else :
        print("good luck to you also but study more")
except Exception as e:
    print("Input is not a number !")