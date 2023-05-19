import sys

a,b = map(int,sys.stdin.readline().rstrip().split())

aa = []
bb=[]
for i in range(a) :
    aa.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(a) :
    bb.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(a) :
    for j in range(b) :
        print(aa[i][j]+bb[i][j],end=' ')
    print()