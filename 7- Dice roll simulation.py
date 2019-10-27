#!usr/bin/env python3
# -*- coding:utf-8 -*-

'''
A die simulator generates a random number from 1 to 6 for each roll. 
You introduced a constraint to the generator such that it cannot roll 
the number i more than rollMax[i] (1-indexed) consecutive times. 

https://leetcode.com/problems/dice-roll-simulation/discuss/404840/Short-Python-DP-with-detailed-image-explanation
'''
def dieSimulator(n, rollMax):
    dp=[[0 for i in range(7)] for k in range(n+1)]
    dp[0][-1]=1

    for row in range(1,n+1):
        for col in range(6):
            for j in range(1,rollMax[col]+1):
                if j<=row:
                    dp[row][col]+=dp[row-j][6]-dp[row-j][col]
        dp[row][6]=sum(dp[row])
    
    return dp[-1][-1]%(10**9+7)

