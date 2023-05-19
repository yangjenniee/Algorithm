import sys

n= int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip().split()))
so = 0
for i in a :
    cnt = 0
    for j in range(1,i+1) :
        if i%j == 0 :
          cnt+=1
    if cnt==2:
        so +=1
print(so)

