import sys

n,k = map(int,sys.stdin.readline().rstrip().split())
arr = [i for i in range(1,n+1)] #처음에 앉아있는 사람들의 리스트
answer=[] #제거된 사람들이 들어갈 배열
num=0 #제거할 사람의 인덱스

for j in range(n) :
    num += k-1 #인덱스는 1씩 앞이므로
    if num>=len(arr) :
       num= num%len(arr) #한 바퀴 돌았을 때 num이 사람들이 있는 리스트보다 클 때를 대비
    answer.append(str(arr.pop(num)))

print("<",", ".join(answer),">",sep='')


