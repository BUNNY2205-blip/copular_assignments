#Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.
a1 = input("Enter the name of the student::")
b = input("Enter the class of the student::")
print("Enter the marks of the subject out of 100---->")
c = int(input("Enter the marks of the maths subject::"))
d = int(input("Enter the marks of the hindi subject::"))
e = int(input("Enter the marks of the english subject::"))
f = int(input("Enter the marks of the science subject::"))
g = int(input("Enter the marks of the french subject::"))
sum = c+d+e+f+g
a = sum/5
print(f"The sum and percentage of all the subjects of the student {a1} of class {b} are {sum} and {a}")
if a > 60:
    print("Grade A")
elif a > 50:
    print("Grade B")
elif a > 33:
    print("Grade C")
else:
    print("FAIL")