#to find the second largest value in the list
l = [12,4,45,22,45,7,767]
maxv = l[0]
s_max = l[0]
for i in range(len(l)):
    if l[i]>maxv:
        maxv=l[i]
print("The maximum value is",maxv)
for i in range(len(l)):
    if l[i] > s_max and l[i] < maxv:
        s_max=l[i]
print("The second largest value of the list is::",s_max)
