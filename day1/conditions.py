# if - elif - else
mark = float(input("enter mark :"))
if(mark > 90):
    print("grade : O")
elif(mark > 80):
    print("grade : A+")
elif(mark > 70):
    print("grade : A")
elif(mark > 60):
    print("grade : B+")
elif(mark > 50):
    print("grade : B")
elif(mark > 30):
    print("grade : C")
else:
    print("result : Fail")

# match case
mark = float(input("enter mark :"))

match mark:
    case m if mark > 90:
        print("grade : O")
    case m if mark > 80:
        print("garde : A+")
    case m if mark > 70:
        print("grade : A")
    case m if mark > 60:
        print("grade : B+")
    case m if mark > 50:
        print("grade : B")
    case m if mark > 30:
        print("grade : C")
    case _:
        print("result : Fail")
