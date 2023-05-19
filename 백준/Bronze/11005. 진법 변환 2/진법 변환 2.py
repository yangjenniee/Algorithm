import sys

n,b = map(int,sys.stdin.readline().rstrip().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer=''

while n!=0 :
    answer += str(number[n%b])
    n=n//b
print(answer[::-1])

