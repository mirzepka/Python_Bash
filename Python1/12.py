import os
import random
 
def mac(x,y):
    i=0
    while i<y:
        j=0
        while j<x:
            yield random.randint(0,255)
            j+=1
        i+=1
x=128
y=128
mat1=mac(x,y)
mat2=mac(x,y)
mat=[[0 for a in xrange(x)] for b in xrange(y)]
for i in xrange(y):
    for j in xrange(x):
        mat[i][j]=next(mat1)+next(mat2)
print mat[:]
 
