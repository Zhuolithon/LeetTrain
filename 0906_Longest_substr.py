#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:43:22 2019

Given a string, find the length of the longest substring without repeating 
characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        output=0
        track=""
        for char in s:
            if char not in track:
                track+=char
            else:
                while(True):
                    if track[0]==char:
                        track=track[1:]
                        track+=char
                        break
                    else:
                        track=track[1:]
            if len(track)>output:
                output=len(track)
        return output

