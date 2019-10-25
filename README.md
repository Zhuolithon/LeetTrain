# Leetcode training

## 4b- Chess game with knights   
There are two knights walking towards each other. And you need to report the minimum steps for knight 1 to catch knight 2 (by parameter white_cap=1), otherwise the opposite. And also, please report how many ways that k1 could catch k2.  
```
#!usr/bin/env python3
# -*- coding:utf-8 -*-

# First, let's figure out all possible paths that connect pos1 and pos2
    # By symmetry, a->b is the same as b->a
# Second, we need to add an step if white_cap=1 but quickest step number is even
def Knight2(N,white_pos,black_pos,white_cap):
    changes=[[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    w=white_pos
    b=black_pos

    # status at beginning
    last_freq={}
    last_freq[w]=[1,0]   # [a,b] a for ways that could arrive at this point, b for # of steps

    # Let's start on 1st part
    catch_it=0
    step=0
    while not catch_it:
        # every loop makes step +1
        step+=1
        freq={}
        for i in last_freq.keys():
            # possible moves
            temp=[(i[0]+x[0],i[1]+x[1]) for x in changes]
            # delete steps out of the N*N chess
            temp2=[x for x in temp if (x[0]>=0 and x[1]>=0 and x[0]<=N-1 and x[1]<=N-1)]
            for point in temp2:
                # freq: (num of ways arrive at point, steps taken)
                if point in freq:
                    freq[point][0]+=last_freq[i][0]
                    freq[point][1]=step
                else:
                    freq[point]=[last_freq[i][0],step]
        last_freq=freq
        
        # if we set white_cap=1, which means white captures black
        # we need steps to be odd
        if white_cap==1 and b in last_freq and step%2==1:
            catch_it=1
        if white_cap==0 and b in last_freq and step%2==0:
            catch_it=1
        
        # impossible to catch: k moves =(distance^2 / 1^2+2^2)
        if step/2>((b[0]-w[0])**2+(b[1]-w[1])**2)/5 and catch_it==0:
            return (-1,-1)
    
    return last_freq[b]
```


## 4- Chess game with knights  
```
# N*N chess
# K moves
# (r,c) initial position
def knightProbability(N, K, r, c):
    changes=[[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    init=(r,c)
    
    # init freq
    last_freq={}
    last_freq[init]=1
    for move in range(K):
        freq={}
        # K moves begin from keys in last dict
        for i in last_freq.keys():
            temp=[(i[0]+t[0],i[1]+t[1]) for t in changes]
            temp2=[x for x in temp if (x[0]>=0 and x[1]>=0 and x[0]<=N-1 and x[1]<=N-1)]
            for point in temp2:
                if point in freq:
                    freq[point]+=1*last_freq[i]
                else:
                    freq[point]=1*last_freq[i]
        last_freq=freq

    total=0
    for i in last_freq.keys():
        total+=last_freq[i]
    print total/8.0**K
```

## 3- Max points on a line
```
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        
        # max points in a line
        maxnum=0
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                # count numbers in every line
                counts=0
                if points[i][0]-points[j][0]==0:
                    for point in points:
                        if point[0]==points[i][0]:
                            counts+=1                    
                else:
                    k=(points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    for point in points:
                        if point[1]==k*(point[0]-points[i][0])+points[i][1]:
                            counts+=1
                if counts>maxnum:
                    maxnum=counts
        return maxnum
```


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