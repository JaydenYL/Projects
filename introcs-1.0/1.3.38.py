#sine.py
#YULIU
#2019.7.30

import sys
import stdio
import math

times = 24
x= float(sys.argv[1])*math.acos(-1)
sinx = 0
i = 1
while i <=times + 1:
    fac = j = 1
    t = 2*i - 1
    #print(t)
    while j <= t:
        fac *= j
        j += 1
    #print(fac)
    an = (-1)**(i-1)*(x**t)/fac
    sinx += an
    i += 1
format = '%.6f\n'
stdio.writef(format,sinx)
    
    
