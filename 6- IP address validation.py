#!usr/bin/env python3
# -*- coding:utf-8 -*-

import re
number = int(input())

for n in range(number):
    line=input()

    # test IPv4
    if "." in line:
        splitline=line.split(".")
        temp=[]
        if len(splitline)==4:
            for num in splitline:
                try:
                    if int(num)>=0 and int(num)<=255:
                        temp.append(num)
                except:
                    pass
        if len(temp)==4:
            print("IPv4")
            continue
        
    # test IPv6
    if ":" in line:
        splitline=line.split(":")
        if '' in splitline:
            tag=1
        else:
            tag=0
        for i in splitline:
            if "".join(re.split("[^g-zG-Z]*", i))!='':
                splitline.remove(i)
        if (tag==0 and len(splitline)==8) or tag==1:
            print("IPv6")
            continue

        
    # Neither
    print("Neither")


                
