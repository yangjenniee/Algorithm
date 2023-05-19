import sys

a,b = map(int,sys.stdin.readline().rstrip().split())
yak = [0]*b
cnt=0
i=0
while True :
    i+=1
    if a%i == 0 :
        yak[cnt]=i
        cnt+=1
        if cnt==b or yak[cnt-1]==a :
            break
print(yak[b-1])
