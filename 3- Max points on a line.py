#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        
        # max points in a line
        maxnum=0
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                # count numbers in every line
                counts=0
                if points[i][0]-points[j][0]==0:
                    for point in points:
                        if point[0]==points[i][0]:
                            counts+=1                    
                else:
                    k=(points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    for point in points:
                        if point[1]==k*(point[0]-points[i][0])+points[i][1]:
                            counts+=1
                if counts>maxnum:
                    maxnum=counts
        return maxnum