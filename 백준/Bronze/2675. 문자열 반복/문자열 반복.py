import sys

t=int(sys.stdin.readline())
for i in range(t) :
    r,s=sys.stdin.readline().rstrip().split()
    r= int(r)
    for a in s :
        for j in range(r) :
            print(a,end="")
    print()

