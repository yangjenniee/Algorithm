import sys
a = int(sys.stdin.readline())
sum=0

for i in range(1,a+1) :
  b,c = map(int,sys.stdin.readline().split())
  sum = b+c 
  print("Case #",sep="",end="")
  print(i,sep="",end="")
  print(": ",end="")
  print(b,"+",c,"=",sum)
  