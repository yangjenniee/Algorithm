h,m,z=map(int,input().split())
price = 0 
max = 0

if h==m==z :
  price = 10000+h*1000

elif h==m or h==z :
  price = 1000+h*100

elif m==z :
  price = 1000+m*100

else :
  max=h
  for i in range(2):
    if max<m :
      max=m
    elif max<z :
      max=z 
    price = max*100

print(price)
  

