#4) Create a billing program using list. Program should have options to 
#1. Create Bill
#2. Display Item Price and total bill amount
#3. Display Total
#4. Exit
item = []
price = []
sum = 0
while True:
    print("\n Billing menu::")
    print("\n 1. Create Bill")
    print("\n 2. Display Item Price and Total Bill Amount")
    print("\n 3. Display Total Only")
    print("\n 4. Exit")
    a = int(input("Enter your choice to get the desired operation::"))
    if a ==1:
        n = int(input('How many items do you want to add in the list::'))
        for i in range(n):
            items = (input("Enter item name::"))
            prices = float(input(f"Enter the price of the item ::{item}::Rs->"))
            item.append(items)
            price.append(prices)
        print("Items added successfully in your bill!!")
    elif a==2:
        if n==0:
            print("There are NULL items in the bill!!")
        else:
            print("\n Item list::")
            print(item," --->",price)
    elif a ==3:
        if n==0:
            print("There are NULL elements in the bill:")
        else:
            for i in range(len(price)):
                sum=sum+price[i]
            print("The sum of the bill is::",sum)

    elif a ==4:
        print("Thank you for visiting the portal")
        break
    else:
        print("Invalid choice please check again::")

