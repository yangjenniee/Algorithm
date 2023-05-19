import sys

a = int(sys.stdin.readline())
s=""
b=a*2

for i in range(1,(b),2) :
    print(" "*(a-1)+"*"*(i))
    a=a-1
for i in range(b-3,0,-2) :
    print(" "*(a+1)+"*"*(i))
    a=a+1