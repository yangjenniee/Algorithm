import sys

h,s = map(int,sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline())

ss = s+m
hh=h


if ss>=60 :
    hh+=ss//60
    ss=ss%60
if hh>=24 :
    hh-=24


print(hh,ss)

