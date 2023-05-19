import sys
n,m = map(int,sys.stdin.readline().split())
lst = [0 for _ in range(n+1)]

for i in range(m) :
    a,b,c=map(int,sys.stdin.readline().split())
    for x in range(a,b+1) :
        lst[x]=c

for i in range(1,n+1) :
    print(lst[i] ,end=" ")