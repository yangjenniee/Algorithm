import sys

n=int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().rstrip()))
sum=0
for i in lst:
    sum+=i
print(sum)