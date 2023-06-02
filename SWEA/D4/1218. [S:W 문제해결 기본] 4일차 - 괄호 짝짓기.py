import sys

sys.stdin = open("input.txt","r")
t = 10 #테스트케이스가 10개이므로

for tc in range(t) :
    n = int(input()) #테스트케이스의 길이
    lst = list(map(str,input())) #테스트케이스
    stck = []

    #왼쪽 괄호
    left = ['(','{','[','<']
    #오른쪽 괄호
    right = [')','}',']','>']

    for i in range(n) :
        if lst[i] in left :
            stck.append(lst[i])
        if lst[i] in right :
            #가장 상위의 괄호값과 쌍이라면
            if right.index(lst[i]) == left.index(stck[-1]) :
                #상위의 원소 제거하기
                stck.pop()
            else : #짝이 아니면 종료
                break
        res = 0
    if len(stck) == 0 :
        res = 1

    print("#{} {}".format(tc+1,res))
