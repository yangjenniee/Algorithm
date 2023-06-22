import sys

def solution(properties,location) :
    #enumerate() : 이넥스와 값을 함께 반환
    #enumerate(properties) : properties 리스트의 각 요소에 대해 인덱스와 값을 반환
    #리스트 컴프리헨션 : [표현식 for 항목 in 반복가능객체 if 조건(선택사항)]
    #enumerate(properties) 는 반복 가능한 객체
    #(i,p)라는 튜플 생성 이를 리스트에 추가
    # i : enumerate(properties) : 반환된 요소의 인덱스 나타냄
    # p : properties 의 리스트의 각 요소를 나타냄
    # properties가 [10,20,30]으로 주어지면 '(0,10)','(1,20)' ,,, 튜플  반환
    # 각 반환된 튜플은 '(i,p)' 형태로 리스트 컴프리헨션에 의해 생성된다
    # 따라서 queue 리스트는 [(0,10),(1,20),(2,30)] 이 된다.
    queue = [(i,p) for i,p in enumerate(properties)]
    answer = 0
    while True :
        cur = queue.pop(0)
        #any() : list의 원소를 필터링하거나 조건 검사할 때 사용하는 함수
        #queue 모든 튜플을 순회하면서 순회 중 튜플의 우선순위가 현재 프로세스에서 pop한 cur 튜플의
        #우선순위보다 큰지 확인
        #조건을 만족하면 queue에 현재 프로세스를 다시 집어넣기

        if any(cur[1] <q[1] for q in queue) :
            queue.append(cur)
        else :
            answer += 1
            if cur[0] == location :
                return answer

