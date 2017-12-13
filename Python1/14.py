import os
import random

x=3
y=3
mat=[[random.randint(-2,2) for osX in xrange(x)] for osY in xrange(y)]
wyz=0
for i in xrange(y):
    for j in xrange(x):
        for k in xrange(x):
            a=1
            b=1
            print ""
            for l in xrange(x):
                print (i+l)%x
                a*=mat[(i+l)%x][(j+l)%y]
                b*=mat[(i-l)%x][(j+l)%y]
            wyz+=a-b

for row in mat:
    for val in row:
        print '{:4}'.format(val),
    print ""
print "Wyznacznik :"+str(wyz)
 
