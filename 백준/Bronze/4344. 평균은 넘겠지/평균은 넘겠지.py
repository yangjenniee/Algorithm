import sys

a = int(sys.stdin.readline().rstrip())

for _ in range(a) :
    list1 = list(map(int,sys.stdin.readline().rstrip().split()))
    avg = sum(list1[1:])/list1[0]
    cnt = 0
    for score in list1[1:] :
        if score > avg :
            cnt+=1
        rate = cnt /list1[0] * 100
    print(f'{rate:.3f}%')






