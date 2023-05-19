import sys

n=int(sys.stdin.readline())
for _ in range(n) :
    s = sys.stdin.readline().rstrip().split()
    for i in s :
        for j in reversed(i) :
            print(j,end='')
        print(end=" ")
