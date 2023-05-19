import sys

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = sys.stdin.readline().rstrip()
cnt=0
for i in cro :
    a=a.replace(i,'a')
print(len(a))











