import sys

n = int(sys.stdin.readline())
queue = []
for i in range(n):
    a = sys.stdin.readline().rstrip().split()
    order = a[0]
    if order == 'push' :
        queue.append(a[1])
    elif order == 'pop' :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue.pop(0))
    elif order == 'size' :
        print(len(queue))
    elif order == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif order == 'front' :
        if len(queue) == 0:
            print(-1)
        else :
            print(queue[0])
    elif order == 'back' :
        if len(queue) == 0:
            print(-1)
        else :
            print(queue[-1])


