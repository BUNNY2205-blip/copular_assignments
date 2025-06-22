def add(a,b):
    res = a+b
    print("sum is::",res)

def sub(a,b):
    res1=a-b
    print("Subtraction is::",res1)

def multi(a,b):
    res2=a*b
    print("Multiplication is::",res2)

def div(a,b):
    res3=a/b
    print("Division is::",res3)

a = int(input("Enter the first number you want in the operation::"))
b = int(input("Enter the second number you want in the operation::"))
while True:
    print(''' 1. Input 1 for addition
    2. Input 2 for subtraction
    3. Input 3 for multiplication
    4. Input 4 for division
    5. Input 5 to exit the calculator''')
    c = int(input("Enter the value for the desired opertation::"))
    if c==1:
        add(a,b)
    elif c==2:
        sub(a,b)
    elif c==3:
        multi(a,b)
    elif c==4:
        div(a,b)
    elif c==5:
        print("You are out of the calculator")
        break
    else:
        print("Invalid input oops!!")


