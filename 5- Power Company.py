#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
n=14  
Model=[3,4,6,11,9,9,9,9,8,8,8,8,8,8]  
There are 14 generators, and we need to turn off ceiling(n/2). One of the most 
optimal solution is to turn off model 8 and 9. By deactivate 8 and 9, we turn 
off 4+6=10 generators
'''

import math

def deactivate(n,models):
    dictmodel={}
    # turn models list into dict
    for i in models:
        if i in dictmodel:
            dictmodel[i]+=1
        else:
            dictmodel[i]=1
    dictmodel=sorted(dictmodel.items(),key=lambda x:x[1],reverse=True)

    # requirements
    half=math.ceil(n/2)

    # run loop to find out when the requirements are satisfied
    turnoff=0
    needtodo=0
    for i in dictmodel:
        turnoff+=i[1]
        needtodo+=1
        if turnoff>=half:
            break
    
    return needtodo
















