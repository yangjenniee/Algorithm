def solution(arr):
    a=[]
    for i in arr :
        if a[-1:]== [i] : #마지막 원소의 리스트와 i값 리스트와 비교 
            continue # 값이 같으면 다음 반복문 
        else :
            a.append(i) #아니면 추가 

    return a



