
a=[]
b=[]
for i in range(1,31) :
    a.append(i)

for i in range(28) :
    b.append(int(input()))

set1 = set(a)
set2 = set(b)
set3=sorted(set1-set2)

for i in set3 :
    print(i)


