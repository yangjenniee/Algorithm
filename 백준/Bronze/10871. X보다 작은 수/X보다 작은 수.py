a,b = map(int,input().split())
list1 = list(map(int,input().split()))
s=""

for i in list1 :
  if i<b :
    s+=str(i)
    s+=" "

print(s)
    
  