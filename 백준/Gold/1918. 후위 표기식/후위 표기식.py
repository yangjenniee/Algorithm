import sys

icp = {'(' :3, '*':2, '/':2, '+':1,'-':1}
isp = {        '*':2, '/':2, '+':1,'-':1, '(' :0}

word = sys.stdin.readline().rstrip()

equ =''
stk = []

for ch in word :
    if ch.isalpha() : #알파벳일 경우
        equ+=ch
    else :
        if ch == ')' :
            while stk:
                t = stk.pop()
                if t =='(' :
                    break
                else :
                    equ+=t #equ에 괄호 내 연산자 넣기
        else : #연산자
            while stk and icp[ch] <= isp[stk[-1]] :
                equ+=stk.pop() #우선순위가 큰 연산자를 후위 표기식에 넣기
            stk.append(ch)

while stk :
    equ+= stk.pop()

print(equ)
