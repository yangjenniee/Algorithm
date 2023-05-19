import sys

a=sys.stdin.readline().rstrip()
b=sys.stdin.readline().rstrip()
a=int(a)
b=int(b)
lst = [i for i in range(a,b+1)]
sosu=[]
cnt=0

for i in lst :
    cnt = 0
    for j in range(1,i+1) :
        if i%j==0 :
            cnt+=1
    if cnt==2 :
        sosu.append(i)

if len(sosu)== 0 :
    print("-1")
else :
    print(sum(sosu))
    print(min(sosu))

