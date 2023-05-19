import sys 

a = int(input())
b = list(map(int,input().split()))
c = int(input())
count = 0 

for i in range(a) :
  if b[i]==c :
    count+=1
print(count)
