import sys
import math

def solution(progresses, speeds):
    n = len(progresses) #progresses의 길이 변수화
    date_left = []  #몇 일 남았는지 저장하는 스택
    answer=[]

    for i in range(n):
        progress_left = 100 - progresses[i] #progress가 얼마나 남았는지
        cut = math.ceil(progress_left/speeds[i]) #올림 함수를 이용하여 몫을 구함
        #나머지가 있으면 하루 더 해야하니까 올림 함수 이용한 것
        date_left.append(cut) #해당 몫을 스택에 추가

    # 문제 첫번째 예시라면 date_left = [7,3,9]
    while date_left :
        left = date_left.pop(0) #left = 7 date_left=[3,9]
        result = 1
        #큰 수가 나올 때 까지 계속 result를 더해주기
        while len(date_left) != 0 and left>=date_left[0] :
            result += 1
            date_left.pop(0) #date_left = [9] answer = [2]
        #큰 값을 만나면 탈출
        answer.append(result) 
    return answer