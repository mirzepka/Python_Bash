import os
import random

x=8
y=8
mat1=[[random.randint(-10,10) for osX in xrange(x)] for osY in xrange(y)]
mat2=[[random.randint(-10,10) for osX in xrange(x)] for osY in xrange(y)]
result=[[ 0 for osX in xrange(x)] for osY in xrange(y)]

for i in xrange(y):
    for j in xrange(x):
        for l in xrange(x):
            result[i][j]+=mat1[l][j]*mat2[i][l]

for row in mat1:
    for val in row:
        print '{:4}'.format(val),
    print ""
print ""
for row in mat2:
    for val in row:
        print '{:4}'.format(val),
    print ""
print ""
for row in result:
    for val in row:
        print '{:4}'.format(val),
    print ""

