#to find the minimum in a list
l = [1,23,35,-1,34,4,65]
min = l[0]
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
print("The minimum value is::",min)
    