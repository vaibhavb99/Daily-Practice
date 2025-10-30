#2.wap to check if the student has scored 70% print "good luck" (take user input)
try:
    score = eval(input("Enter your percentage: "))
    if score >=70:
        print("good luck !")
    else :
        print("good luck to you also but study more")
except Exception as e:
    print("Input is not a number !")