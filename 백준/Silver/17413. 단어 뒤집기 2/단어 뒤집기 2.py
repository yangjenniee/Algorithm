import sys
word = list(sys.stdin.readline().rstrip())

i=0
start=0

while i <len(word) :
    if word[i] == '<' : # 열린 괄호를 만나면
        i+=1
        while word[i] != '>' : #닫힌 괄호를 만날 때 까지
            i+=1
        i+=1 #닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다.
        #isalnum() = 영문, 숫자로만 구성된 경우 True 반환
    elif word[i].isalnum(): #숫자나 알파벳을 만나면
        start = i
        while i <len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] #숫자,알파벳 범위에 있는 것들을
        tmp.reverse() #뒤집는다
        word[start:i] = tmp
    else : #괄호도 아니고, 알파벳, 숫자도 아니면 즉 공백
        i+=1 #그냥 증가

print("".join(word)) #word를 문자열로 합쳐서 반환 




