import sys

aa=[]
max=-1
maxi=[]
a=0
b=0
for i in range(9) :
    aa.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(9) :
    for j in range(9) :
        if max<aa[i][j] :
            max = aa[i][j]
            a=i+1
            b=j+1
print(max)
print(a,b)
