import sys

dial = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

al = sys.stdin.readline()
result=0
for x in al :
    for j in dial :
        if x in j :
            result+=dial.index(j)
            result+=1
print(result)
