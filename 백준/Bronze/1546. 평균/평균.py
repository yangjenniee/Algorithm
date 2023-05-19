s = int(input())
ss = list(map(int,input().split()))
ma = max(ss)
sum=0
avg = 0

for i in range(s) :
    ss[i] = ss[i]/ma*100

for i in range(s) :
    sum = ss[i]+sum
    avg = sum/s

print(avg)

