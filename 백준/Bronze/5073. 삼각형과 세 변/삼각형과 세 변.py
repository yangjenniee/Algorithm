import sys
while True :
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    if sum(a) ==0 :
        break

    if sum(a)-max(a)<=max(a) :
        print('Invalid')
    elif a[0]==a[1]==a[2] :
        print('Equilateral')
    elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2] :
        print('Isosceles')
    else :
        print('Scalene')


