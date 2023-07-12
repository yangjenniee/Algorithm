def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)] #길이가 n인 0으로 채워진 리스트가 만들어진다
    st = [] #아직 떨어지지 않은 시간들의 모임(index)

    for i in range(n) :
        # prices [1,2,3,2,3]
        # st []
        #없으므로 i append st[0]
        #1>2 이므로
        #st[0,1]
        #2>3
        #st[0,1,2]
        #i=3
        #3>2 이므로 해당됨
        #3에서 2로 가격이 내려간것이므로 2초일때 1초만에 가격이 내려간 것임
        # answer = [0,0,0,0,0]
        #st에서 삭제됨 st [0,1 ]
        #top = 2
        #answer = [0,0,1,0,0] 이 됨
        #그 후 다시 올라와서 1일때도 비교 2는 더 크지 않으므로 3을 append
        # st = [0,1,3]
        # i = 4
        # 떨어지지 않았으므로 st = [0,1,3,4]

        #지금 현재 가격보다 제일 마지막에 있는 가격이 더 크면
        while st and prices[st[-1]] > prices[i] :
            top = st.pop() #주식이 내린것이무로 pop
            answer[top] = i-top #떨어지지 않은 시간
        st.append(i)

    while st :
        top = st.pop()
        answer[top] = n - top - 1
            #top = 4
            #st = [0,1,3]
            # n = 5    5-4-1 = 0
            #answer = [0,0,1,0,0]
            #top = 3
            #st = [0,1]
            # n =5 5-3-1 = 1
            # answer = [0,0,1,1,0]
            # top = 1
            # n = 5 5-1-1 =3
            # answer = [0,3,1,1,0]
    return answer
