import sys
lst=[]
x=[0 for i in range(3)]
y=[0 for i in range(3)]
countx=0
county=0
indexx=0
indexy=0
for i in range(3) :
    z,k= map(int,sys.stdin.readline().rstrip().split())
    lst.append(z)
    lst.append(k)

x[0] = lst[0]
x[1] = lst[2]
x[2] = lst[4]
y[0] = lst[1]
y[1] = lst[3]
y[2] = lst[5]

for i in x :
    countx = x.count(i)
    if countx==1 :
        indexx = x.index(i)

for i in y :
    county = y.count(i)
    if county==1 :
        indexy = y.index(i)

print(x[indexx],y[indexy])


