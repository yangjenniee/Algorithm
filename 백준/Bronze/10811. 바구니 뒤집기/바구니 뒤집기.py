import sys
n,m = map(int,sys.stdin.readline().split())
lst = [i for i in range(n+1)]
for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    temp=lst[a:b+1]
    temp.reverse()
    lst[a:b+1] = temp

for i in range(1,n+1) :
    print(lst[i],end=" ")