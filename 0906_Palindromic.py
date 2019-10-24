#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:52:07 2019

@author: zhuoli

Given a string s, find the longest palindromic substring in s. np.array([0])
np.array([0])

You may assume that the maximum length of s is 1000.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens=len(s)
        if lens==0:
            return ""
        else:
            for i in range(lens):
                for j in range(i+1):
                    test=s[j:lens-i+1+j]
                    if test==test[::-1]:
                        return test
        return output
    
    
    
    
    
    
    
    
    
    
    