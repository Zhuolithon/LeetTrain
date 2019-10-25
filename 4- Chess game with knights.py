#!usr/bin/env python3
# -*- coding:utf-8 -*-

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