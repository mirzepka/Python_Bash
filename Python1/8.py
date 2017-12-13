import os
import random
 
def quick(lis):
    less = []
    equal = []
    greater = []

    if len(lis) > 1:
        pivot = lis[0]
        for x in lis:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick(less)+equal+quick(greater) 
    else:  
        return lis


lis=random.sample(xrange(100), 50)
lis2=lis[:]
print lis
lis=quick(lis)
lis2.sort()
print lis
if len([i for i,j in zip(lis,lis2) if i!=j])==0:
    print "Correct"


