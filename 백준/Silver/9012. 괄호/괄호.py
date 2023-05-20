import sys

def solve() :
    data=sys.stdin.readline().rstrip()
    stack = [] #스택으로 해결, 빈스택 생성
    for item in data : #입력값을 앞에서 부터 하나씩 돌면서 테스트
        if item=='(' : #여는 괄호 일 경우
            stack.append(item) #스택에 집어넣기
        else :
            if len(stack) == 0 : # 스택 길이가 0 이라는 것은 유효한 괄호쌍이 아니라는 것
                print('NO')
                return #종료
            else: #스택이 있을 경우
                stack.pop()  #하나를 뽑아내기
    #for 문을 다 돌았을 때 유효한 경우 스택 길이가 0이어야함
    if len(stack) == 0 :
        print('YES')
    else :
        print('NO')



t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    solve()

