import sys

a = list(map(int,sys.stdin.readline().rstrip().split()))
chess = [1,1,2,2,2,8]
s=[0]*6

for i in range(6) :
    if a[i]!=chess[i] :
        s[i] = chess[i]-a[i]

for i in s :
    print(i ,end=' ')


