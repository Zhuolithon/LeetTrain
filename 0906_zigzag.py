#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:50:13 2019

@author: zhuoli
"""

class Solution:
    def convert(self, s: str, n: int) -> str:
        L,S,j=len(s),['']*numRows,0
        if s=="" or L==1 or numRows==1:
            return s
        init_=1
        move=1        
        for i in range(L):
            S[j]=S[j]+s[i]
            if init_==0 and (j==0 or j==numRows-1):
                move*=-1
            init_=0
            j+=move
        return "".join(S)