import sys

def solution(s):
    lst=[]
    for i in range(len(s)) :
        if s[i] == '(' :
            lst.append('(')
        elif s[i]==')' and len(lst)!=0:
            lst.pop()
        elif s[i] ==')' and len(lst)==0 :
            return False






    if len(lst) == 0 :
        print("True")
        return True
    else :
        print("False")
        return False
