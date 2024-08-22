mark = int(input("Enter a studnet's marks: "))

while mark < 0:
    mark = input("Enter a studnet's marks: ")              

def check_grade(mark):
    grade = ""
    if 80 <= mark <= 100:
        grade = "A"
    elif 70 <= mark < 80:
        grade = "B"
    elif 60 <= mark < 70:
        grade = "C"
    elif 50 <= mark < 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print("Grade : ",check_grade(mark))
