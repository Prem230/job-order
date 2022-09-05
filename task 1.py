n= int(input("enter the lenght of the array:"))
a=[]
for i in range(n):
    a.append(int(input("enter the no:")))
print("the first array:",a)
m = int(input("enter the value:"))
g = []
for y in a:
    if y >= m:
        z = (y+1)
        print(z)
        g.append(z)
    else:
        g.append(y)
print(g)







