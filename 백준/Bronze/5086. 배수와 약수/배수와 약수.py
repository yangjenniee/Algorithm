import sys

i=0
while True :
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if a<b :
        while True :
            i+=1
            c=a*i
            if c==b :
                print("factor")
                i = 0
                break
            if c>b and c!=b :
                print("neither")
                i=0
                break
    if a>b :
        while True :
            i+=1
            c=b*i
            if c==a :
                print("multiple")
                i = 0
                break
            if c>a and c!=a :
                print("neither")
                i=0
                break
    if a==0 and b==0 :
        break