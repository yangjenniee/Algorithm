import sys

n=int(sys.stdin.readline())
stack=[]
for i in range(n) :
    a=sys.stdin.readline().split()
    order = a[0]
    if order == 'push' :
        stack.append(a[1])
    elif order == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
    elif order == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif order == 'size' :
        print(len(stack))
    elif order == 'empty' :
        if len(stack)==0 :
            print(1)
        else :
            print(0)

