import subprocess

score = int (input("what is your score?"))
grade = "not graded"
if 90 <= score <= 100:
    grade = "A"
    print("grade : A")
    print("excellent, star")

elif 80 <= score <= 90:
    grade = "A-"
    print("grade : A-")
    print("congratulations, you made it")


elif 60 <= score <= 70:
    grade = "B"
    print("grade:B")
    print("Very good, hardwork has paid")

elif 50 <= score <= 60:
    grade = "C"
    print("grade:C")
    print("You are above average, congratulations")

elif 40<= score <=50:
    grade = "D"
    print("grade:D")
    print("You need a performance improvement plan")

elif 100 < score or 0 > score:
    print("Error!!")
    print("Please check your grade with your moderator \n""Sorry")

else:
    print("FAIL")
    grade = "FAIL"
    print("Work harder")

subprocess.run (["python", "KCSE GRADING.py"])