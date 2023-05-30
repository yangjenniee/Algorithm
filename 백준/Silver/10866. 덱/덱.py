import sys

n = int(sys.stdin.readline())
lst=[]
for i in range(n) :
    a = sys.stdin.readline().rstrip().split()
    str = a[0]
    if str == 'push_front' :
        lst.insert(0,int(a[1]))
    elif str == 'push_back' :
        lst.append(int(a[1]))
    elif str == 'pop_front' :
        if len(lst) == 0:
            print(-1)
        else :
            print(lst.pop(0))
    elif str == 'pop_back' :
        if len(lst) == 0:
            print(-1)
        else :
            print(lst.pop(-1))
    elif str == 'size' :
        print(len(lst))
    elif str == 'empty' :
        if len(lst)==0 :
            print(1)
        else :
            print(0)
    elif str == 'front' :
        if len(lst)== 0:
            print(-1)
        else :
            print(lst[0])
    else :
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])


