import sys
sys.stdin = open("input.txt", "r")

T = 10 #테스트 케이스가 10개이므로
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst=list(map(int,input().split()))
    ans = 0
    #좌우 2개 최대값 찾기
    for i in range(2,n-2) : #인덱스 2번부터
        max=lst[i-2] #초기값, 더큰값오면 갱신됨
        for j in range(i-1,i+3) :
            if j == i  :
                continue #자기자신은 제외
            else :
                if max<lst[j] :
                    max =lst[j]
        if lst[i] > max :
            ans+=lst[i] - max # 값 누적
    print(f'#{test_case} {ans}')