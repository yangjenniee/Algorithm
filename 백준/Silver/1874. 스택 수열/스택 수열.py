import sys

n = int(sys.stdin.readline().rstrip())
stack=[]
answer=[]
flag = 0
cur=1
for i in range(n) :
    num = int(sys.stdin.readline().rstrip())
    while cur<=num : #입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
    # 입력한 수 만나면 while 문 끝
        cur+=1

    if stack[-1] == num : # 스택의 top와 입력한 숫자가 같다면
        stack.pop() #스택 pop으로 수열 만들기
        answer.append("-")
    else :
#스택의 top가 입력한 수가 아니면 주어진 스택 만들 수 없다.
#top이 num보다 크면 num은 top보다 더 아래에 있음
        print('NO')
        flag=1
        break
if flag==0 :
    for i in answer :
        print(i)



