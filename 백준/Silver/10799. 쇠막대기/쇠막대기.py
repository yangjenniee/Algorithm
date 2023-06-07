import sys

bar_razor = list(sys.stdin.readline().rstrip()) #입력 받기
answer = 0
st = []

for i in range(len(bar_razor)) : #bar_razor 길이 만큼
    if bar_razor[i] == '(' : #여는 괄호이면
        st.append('(') #스택에 (만 추가
    else : #닫는 괄호이면
        if bar_razor[i-1] == '(' : # 앞이 (면 레이저
            st.pop() #st 가장 상단 값 빼기
            answer += len(st) #스택의 길이만큼 더해주기

        else : #앞이 )면 쇠막대기 끄트머리
            st.pop() #st 가장 상단 값 빼기
            answer += 1 #하나씩만 추가
print(answer)



