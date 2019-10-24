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
        
