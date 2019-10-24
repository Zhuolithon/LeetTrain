# Leetcode training

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