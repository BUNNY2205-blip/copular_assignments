#to find the second minimum value in a list
l = [1,23,35,-1,34,4,-1,65]
min = l[0]
s_min = l[0]
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
print("The minimum value is::",min)
for i in range(len(l)):
    if l[i]<s_min and l[i]>min:
        s_min=l[i]
print("The second minimum value in the list is::",s_min)
    