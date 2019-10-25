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
        

