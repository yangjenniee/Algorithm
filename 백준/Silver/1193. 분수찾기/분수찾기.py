import sys

n=int(sys.stdin.readline().rstrip())
flag = 1
a=0
b=0
while n>flag :
    n-=flag
    flag+=1

if flag%2==0:
    a=n
    b=flag-n+1

else :
     a=flag-n+1
     b=n
print(a,'/',b,sep='')













