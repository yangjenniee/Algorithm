import sys

lst = list(map(int,sys.stdin.readline().rstrip().split()))
a = [0,0,0,0]

for i in lst :
    a[0] = lst[0]-0
    a[1] = lst[1]-0
    a[2] = lst[2]-lst[0]
    a[3] = lst[3]-lst[1]

print(min(a))