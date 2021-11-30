#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    s=bin(n)
    print(s)
    c=0
    o=[]
    for i in range(len(s)):
        if s[i]=='1' and i==len(s)-1:
            print('1stif')
            c+=1
            o.append(c)
            break
        elif s[i]=='1':
            print('2ndif')
            c+=1
        
        else:
            print('else')
            o.append(c)
            c=0
    print(o)            
    print(max(o))