import sys
n = int(sys.stdin.readline())
x = []
y = []
area = 0
for i in range(n) :
    x1,y1 = map(int,sys.stdin.readline().split())
    x.append(x1)
    y.append(y1)

area = (max(x)-min(x))*(max(y)-min(y))
print(area)