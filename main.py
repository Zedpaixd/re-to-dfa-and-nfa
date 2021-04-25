#to form Stack Class
import pandas as pd
import numpy as np
import re
class StackClass:

    def __init__(self, itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def pop(self):
        return self.items.pop()


    def push(self, item):
        self.items.append(item)
        return 0
# Infix to postfix Conversion of the expression given
def infixtopostfix(infixexpr):

    s=StackClass()
    outlst=[]
    prec={}
    # this is the precedence order
    prec['*']=3
    prec['|']=2
    prec['.']=1
    prec['(']=1
    oplst=['*','|','.']

    tokenlst=infixexpr.split()
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outlst.append(token)

        elif token == '(':
            s.push(token)

        elif token == ')':
            topToken=s.pop()
            while topToken != '(':
                outlst.append(topToken)
                topToken=s.pop()
        else:
            while (not s.isEmpty()) and (prec[s.peek()] >= prec[token]):
                #print token
                outlst.append(s.pop())
                #print outlst

            s.push(token)
            #print (s.peek())

    while not s.isEmpty():
        opToken=s.pop()
        outlst.append(opToken)
        #print outlst
    return outlst
    #return " ".join(outlst)
    # extract the keys from the expression as well as the operators

postfix = infixtopostfix("")
regex=''.join(postfix)
# | is for OR, * for Kleene Closure, . is for concatenation
keys=list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'e'))
# e stands for epsilon
# Regex to NFA
s=[];stack=[];start=0;end=1

counter=-1;c1=0;c2=0

for i in regex:
    if i in keys:
        counter=counter+1;
        c1=counter;
        counter=counter+1;
        c2=counter;
        s.append({});
        s.append({})
        stack.append([c1,c2])
        
        s[c1][i]=c2
    elif i=='*':
        r1,r2=stack.pop()
        counter=counter+1;
        c1=counter;
        counter=counter+1;
        c2=counter;
        s.append({});
        s.append({})
        stack.append([c1,c2])
        s[r2]['e']=[r1,c2];s[c1]['e']=[r1,c2]
        if start==r1:
            start=c1 
        if end==r2:
            end=c2 
    elif i=='.':
        r11,r12=stack.pop()
        r21,r22=stack.pop()
        r12 = r11
        r11 = r22
        stack.append([r21,r12])
        elem = s[r12]
        del s[r12]
        for key in elem.keys():
            s[r11][key] = elem.get(key)-1
        counter = counter - 1
        if start==r11:
            start=r21 
        if end==r22:
            end=r12 
    else:
        counter=counter+1;
        c1=counter;
        counter=counter+1;
        c2=counter;
        s.append({});
        s.append({})
        r11,r12=stack.pop()
        r21,r22=stack.pop()
        stack.append([c1,c2])
        s[c1]['e']=[r21,r11]; s[r12]['e']=c2; s[r22]['e']=c2
        if start==r11 or start==r21:
            start=c1 
        if end==r22 or end==r12:
            end=c2

#print(keys)
print(start)
print(end)
for i,x in enumerate(s):
    print(f"{i}: {x}")
# Convert the above s list into a matrix


