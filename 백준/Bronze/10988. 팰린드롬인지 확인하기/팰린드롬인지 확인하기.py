import sys

a = list(sys.stdin.readline().rstrip())
b=a[::-1]

if a==b :
    print("1")
else :
    print("0")