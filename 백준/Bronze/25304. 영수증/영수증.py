a = int(input())
b = int(input())
sum=0
for i in range (b) :
  c,t = map(int,input().split())
  sum+=c*t

if sum == a :
  print("Yes")
else :
  print("No")
  