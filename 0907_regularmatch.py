# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:59:06 2019

@author: zhuoli

Given an input string (s) and a pattern (p), 
implement regular expression matching with support for '.' and '*'.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 0th index represents no charactesr
        # 1st index represents the 1st characters
        match = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        # Matching 0 characters in the string and pattern is true
        match[0][0] = True
        
        # Accounts for all cases where the string is empty and the '*'
        # may match no charactesr
        for p_i in range(len(p)):
            match[p_i + 1][0] = p[p_i] == '*' and match[p_i - 1][0]

        for p_i in range(len(p)):
            for s_i in range(len(s)):
                # Straightforward match
                if self.simpleMatchIdx(s, p, s_i, p_i):
                    match[p_i + 1][s_i + 1] = match[p_i][s_i]

                # Two cases:
                # 1. Skip <character>* altogether and hope that the pattern before that matches the current 
                # 2. Check if <chracter>* matches a single character in s, and potentially more on next iteration
                elif p[p_i] == '*':
                    match[p_i + 1][s_i + 1] = \
                        match[p_i - 1][s_i + 1] or \
                        (match[p_i + 1][s_i] and self.simpleMatchIdx(s, p, s_i, p_i - 1))

        return match[-1][-1]    

    def simpleMatchIdx(self, s, p, s_i, p_i):
        return s_i < len(s) and p_i < len(p) and (p[p_i] == '.' or p[p_i] == s[s_i])