import sys

a = sys.stdin.readline().rstrip()
a=a.upper()
uniq = list(set(a))

cnt = []
for x in uniq :
    ct = a.count(x)
    cnt.append(ct)

if cnt.count(max(cnt)) > 1 :
    print("?")

else :
    index = cnt.index(max(cnt))
    print(uniq[index])