def gen(grades):
    gpa = 0
    for grade in grades:
        gpa += grade
    
    gpa /= len(grades)
    return gpa

grades = []
while True:
    grade = input("input grade or 'exit' to calculate gpa\n>>")
    if grade.lower() == "exit":
        break
    try:
        grade = float(grade)
        if grade > 4.0:
            print("I don't care about you being a nerd keep the number under 4.0")
        elif grade < 0.0:
            print("why do you have a negative grade? honestly im not calculating that")
        else:
            grades.append(float(grade))
    except:
        print("i have no idea what you're saying to me")

half = int(len(grades)/2)
print(f"sem1:{gen(grades[0:half])}\nsem2:{gen(grades[half:-1])}\nall:{gen(grades)}")

dream = input("what gpa would you like?\n>>")
try:
    dream = float(dream)
    gpa = gen(grades)
    if dream > 4.0:
        print("thats not happening")
    elif dream < gpa:
        print("why do you want your gpa to go down")
    else:
        print(f"you need to juice {dream-gpa} more out of your grades")
except:
    print("thats is not happening")