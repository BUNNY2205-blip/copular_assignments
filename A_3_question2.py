#to check the palindrome number
a = int(input("Enter the number you want to check it as palindrome number::"))
print("Your given number is::",a)
original = a
#we need to find the reverse of the number
reverse = 0
while a>0:
    digit = a%10
    reverse=(reverse*10)+digit
    a=a//10
print("The reverse of the given number is::",reverse)
if original==reverse:
    print(f"the given number {original} is equal to the it's reverse {reverse} so it is a palindrome")
else:
    print(f"The given number {original} is not equal to it's reverse {reverse} so it is not a palindrome")
