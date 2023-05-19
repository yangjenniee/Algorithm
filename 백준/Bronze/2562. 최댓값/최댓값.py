import sys

lst = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
max = max(lst)
print(max)
print(lst.index(max)+1)
