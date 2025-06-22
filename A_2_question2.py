#3) Input a number from user and find its factorial using for loop
a = int(input("Enter the number you want the factorial of::"))
for i in range (1,a):
    a=a*i
print(f"Factorial of is {a}")
