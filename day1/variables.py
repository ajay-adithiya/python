# students mark (float)
mark1 = float(input("enter stud1 mark :"))
mark2 = float(input("enter stud2 mark :"))
mark3 = float(input("enter stud3 mark :"))

# students name (str)
stud1 = "viky"
stud2 = "sam"
stud3 = "ram"

# Average marks
avg_marks = (mark1 + mark2 + mark3)/3
print("average mark of students :",avg_marks)

# Type conversion
avg_marks = int(avg_marks)
print(type(avg_marks))

# store marks [Dictionary]
students = {stud1 : mark1 , stud2 : mark2 , stud3 : mark3}
print(students)

# boolean
def is_pass(mark1):
    is_pass = True
    print(is_pass)

if(mark1 >= 30):
    is_pass(mark1)
    
else:
    print("fail")