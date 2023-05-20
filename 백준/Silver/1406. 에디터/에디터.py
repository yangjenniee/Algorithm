import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = [] #커서의 오른쪽 리스트

for _ in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().rstrip().split())
    if command[0]== 'B' : #커서 왼쪽 문자 삭제
        if st1 : #st1 리스트에 값이있으면
            st1.pop() #커서 왼쪽 스택 값 pop
    elif command[0] == "L" : #커서 왼쪽으로 옮기기
        if st1 : #st1 리스트에 값이 있으면
            st2.append(st1.pop()) #커서 오른쪽 스택에 st1의 마지막 값 push
    elif command[0] == "D" : #커서 오른쪽으로 옮기기
        if st2 : #st2 리스트에 값이 있으면
            st1.append(st2.pop()) #커서 왼쪽 스택에 st2의 마지막 값 push
    else : #커서 왼쪽에 값 추가하기
        st1.append(command[1]) #해당 값 추가

#오른쪽 커서 스택의 값을 거꾸로 해서 st1에 원소형태로 추가
st1.extend(reversed(st2))
#리스트를 문자열 형태로 합쳐서 출력
print(''.join(st1))
