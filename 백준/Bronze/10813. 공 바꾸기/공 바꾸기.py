n,m= map(int,input().split()) #바구니 갯수 입력, 횟수 입력
box = [0] * n # 배열의 크기를 바구니의 개수만큼 만들고 0으로 초기화 한다

for i in range(0,n) :
    box[i] = i+1

for i in range(m) :
    a,b=map(int,input().split())
    box[a-1],box[b-1] = box[b-1],box[a-1]

for i in range(n) :
    print(box[i],end=' ')







