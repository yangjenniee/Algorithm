#import sys
#sys.stdin = open("input.txt", "r")


T = 10

pri = {'*':2,'+':1} #우선순위 부여
for test_case in range(1, T + 1):
    N = int(input())
    st = input()
	
    equ = ''
    stk = []

    #[1] 중위 -> 후위표기식
    for ch in st :
        #isdigit() : 숫자인지 알 수 있는 함수
        if ch.isdigit() : #숫자일 경우
            equ+=ch #equ에 추가
        else : #연산자일 경우
           # if not stk : #스택이 비어있을 경우
           #     stk.append(ch) #무조건 추가
           # else :
           #     if pri[ch] > pri[stk[-1]]: #스택 꼭대기의 우선순위보다 우선순위가 더 크다면
           #         stk.append(ch) #push
           #     else :
            while stk and pri[ch] <= pri[stk[-1]] : #스택에 데이터가 있고 현재 우선순위가 스택의 top보다 더 작으면
                #stack 에서 pop해서 계속 equ에 넣어주기
                equ+=stk.pop()
            stk.append(ch) #현재 우선순위 스택에 넣기

    #stk 에 부호가 남아있을 경우
    while stk :
        equ+=stk.pop()


    #[2] 후위연산식 계산
    for ch in equ :
        if ch.isdigit() : #숫자인가 ?
            stk.append(int(ch)) #stk 을 다 비웠으므로 재활용 ..
        else : #만약 연산자라면
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '*' :
                stk.append(op1*op2)
            elif ch == '+' :
                stk.append(op1+op2)


    print(f'#{test_case} {stk.pop()}') #스택에 마지막 숫자가 최종 계산 결과이므로 



