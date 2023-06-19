import sys
n = int(input())
ans = [0] * n  #정답 배열, n 크기 만큼 만들어주기
A = list(map(int,sys.stdin.readline().rstrip().split())) #수열 리스트
myStack = [] #스택 선언

for i in range(n) :
    # 스택이 비지않고 현재 수열값이 top에 해당하는 수열보다 클 때 까지
    while myStack and A[myStack[-1]] < A[i] :  #오큰수 조건
        ans[myStack.pop()] = A[i] #정답 리스트에 오큰수 저장
    myStack.append(i)

while myStack: #스택이 없어질때까지
    ans[myStack.pop()] = -1

for i in ans :
    print(i,end=' ')


