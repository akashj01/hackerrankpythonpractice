#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

s = input()
ord = defaultdict(lambda : 0)
for i in s:
    ord[i] += 1
lislett = []
lisocc = []
lis =[]
for i,j in ord.items():
    lis.append([i,j])
lis.sort()
for [i,j] in lis:
    lislett.append(i)
    lisocc.append(j)


for i in range(3):
    j = lisocc.index(max(lisocc))
    print(lislett[j],lisocc[j])
    lislett.remove(lislett[j])
    lisocc.remove(lisocc[j])