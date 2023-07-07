import sys

n = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip() #후위 표기식을 word 에 저장
num_lst = [0] * n #피연산자값을 저장하기 위한 nun_lst

for i in range(n) :
    num_lst[i] = int(sys.stdin.readline().rstrip()) #피연산자값 받기

stack = []

for i in word :
    if 'A' <= i <= 'Z' : #후위표기식에서 알파벳을 만나면
        stack.append(num_lst[ord(i)-ord('A')])
    else : #연산자를 만나면
        str2 = stack.pop()
        str1 = stack.pop() # stack 리스트의 마지막 2항목을 꺼내와서 계산

    if i == '+' :
        stack.append(str1+str2)
    elif i == '-' :
        stack.append(str1-str2)
    elif i == '*' :
        stack.append(str1*str2)
    elif i == '/' :
        stack.append(str1/str2)
print('%.2f' %stack[0]) #'%.2f' 함수를 통해 소숫점 자릿수 제한