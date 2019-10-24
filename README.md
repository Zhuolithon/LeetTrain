# Leetcode training

## 2- One to all device with minimal time
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def broadcast_time(origin,adjmatrix):
    n=int(adjmatrix.shape[0])

    delivered=origin+[]
    new_added=origin+[]
    # check if all items are deliverable
    while new_added:
        i=new_added.pop(0)
        for j in range(len(adjmatrix[i])):
            if adjmatrix[i][j]!='none' and j not in delivered:
                delivered.append(j)
                new_added.append(j)

    
    if len(delivered)!=n:
        print("Null")
        return
    
    time=0
    # temp record
    record=-100
    for row in origin:
        for col in range(n):
            if adjmatrix[row,col]!='none':
                record=int(adjmatrix[row,col])
                record_xy=[[row,col]]
                break
        if record>0:
            break

    while len(origin)!=n:
        # find out min in array[origin]
        for row in origin:
            for col in range(n):
                if adjmatrix[row,col]!='none' and int(adjmatrix[row,col])<record:
                    record=int(adjmatrix[row,col])
                    record_xy=[[row,col]]
                if adjmatrix[row,col]!='none' and int(adjmatrix[row,col])==record:
                    record_xy+=[[row,col]]

        time+=record
        
        # every number in the matrix minus record
        for row in origin:
            for col in range(n):
                if adjmatrix[row,col]!='none':
                    adjmatrix[row,col]=int(adjmatrix[row,col])-record

        # denote minimun observation as 'none'
        for xy in record_xy:
            if xy[1] in origin:
                adjmatrix[xy[0],xy[1]]='none'
            elif xy[1] not in origin:
                adjmatrix[xy[0],xy[1]]='none'
                origin.append(xy[1])

        record=-100
        for row in origin:
            for col in range(n):
                if adjmatrix[row,col]!='none':
                    record=int(adjmatrix[row,col])
                    record_xy=[[row,col]]
                    break
            if record>0:
                break

    print(time)
    return time
            


origin=[0]
adjmatrix=np.array([['none','none',122,'none'],['none','none','none',50], \
    [341,10,'none',205],[456,'none',186,'none']])
broadcast_time(origin,adjmatrix)
```        


## 1- 3 cards  
Question:  
Three of a kind> One pair> High card  
0-9 for 40 cards

**code**
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# First, count numbers
def p1_win_count(hands):
    p1=hands[:3]
    p2=hands[3:]
    print(p1,"\n",p2)
    dict1={}
    dict2={}
    for i in p1:
        if str(i) in dict1:
            dict1[str(i)]+=1
        else:
            dict1[str(i)]=1

    for i in p2:
        if str(i) in dict1:
            dict2[str(i)]+=1
        else:
            dict2[str(i)]=1
    
    if len(dict1)<len(dict2):
        print("P1 wins")
        return 0
    elif len(dict1)>len(dict2):
        print("P2 wins")
        return 0

    if len(dict1)==len(dict2):
        dict1=sorted(dict1.items(),key=lambda kv:kv[1],reverse=1)
        dict2=sorted(dict2.items(),key=lambda kv:kv[1],reverse=1)
        for i in range(len(dict1)):
            if int(dict1[i][0])>int(dict2[i][0]):
                print("P1 wins")
                return 0
            elif int(dict1[i][0])<int(dict2[i][0]):
                print("P2 wins")
                return 0

hands=[1,3,3,4,4,4]
p1_win_count(hands)
```