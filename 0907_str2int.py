#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:01:24 2019

@author: zhuoli

 String to Integer (atoi)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        d=1
        if len(s)==0:
            return 0
        if s[0]=='-':
            d=-1
            s=s[1:]
        elif s[0]=='+':
            d=1
            s=s[1:]
        try:
            temp=int(s[0])            
        except:
            return 0
        s=s.split(' ')[0]
        if len(s)==0:
            return 0        
        for i in range(len(s)):
            try:
                int(s[i])
            except:
                s=s[:i]
                break
        r=d*int(s)
        if r.bit_length()>=32 and d==1:
            return (2**31-1)
        elif r.bit_length()>=32 and d==-1:
            return -2**31