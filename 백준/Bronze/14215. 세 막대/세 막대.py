import sys
while True :
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    if a[0]==a[1]==a[2] :
        print(sum(a))
        break
    elif sum(a)-max(a)<=max(a) :
        while(sum(a)-max(a)<=max(a)) :
            idx = a.index(max(a))
            a[idx]-=1
        print(sum(a))
        break
    else :
        print(sum(a))
        break




