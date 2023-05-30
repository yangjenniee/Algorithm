import sys
sys.stdin = open("input.txt", "r")

T = 10 #테스트 케이스가 10개이므로
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst=list(map(int,input().split()))
    ans = 0
    #좌우 2개 최대값 찾기
    for i in range(2,n-2):#인덱스 2번부터
        mx = max(lst[i-2:i]+lst[i+1:i+3]) #슬라이싱 결과로 작업
        if lst[i]>mx :
          ans+=lst[i]-mx # 값 누적함
    print(f'#{test_case} {ans}')