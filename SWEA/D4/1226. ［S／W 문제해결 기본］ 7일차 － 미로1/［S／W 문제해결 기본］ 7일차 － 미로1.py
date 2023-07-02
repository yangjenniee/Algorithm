def bfs(si,sj) :
    #[1] q, v[]생성
    q = [] #빈 배열
    v = [[0]*N for _ in range(N)] #0이 N열 N행이 있게 초기화

    #[2] q에 초기데이터 삽입, v 표시
    q.append((si,sj))
    v[si][sj] = 1

    while q : #q에 데이터가 있는 동안
        ci,cj = q.pop(0) #q에 데이터를 꺼내주기
        if arr[ci][cj] == 3 : #목적지라면
            return v[ci][cj] #return 1


        # 네 방향, 범위내, 미방문, 벽이 아니면 방문(q)
        #상,하, 좌,우 네 방향을 돌기
        for di,dj in((-1,0),(1,0),(0,-1),(0,1)) :
            ni,nj = ci+di,cj+dj
            #0보다 크거나 같고 N보다 작고, 미방문이고,벽이 아니면
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj] !=1 :
                q.append((ni,nj))
                v[ni][nj]=1 #방문
    return 0



T = 10
for test_case in range(1,T+1) :
    _ = input()
    N=16
    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 2 :
                si,sj = i,j

    ans = bfs(si,sj)
    print(f'#{test_case} {ans}')

