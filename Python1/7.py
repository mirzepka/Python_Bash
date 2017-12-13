a=int(raw_input("a: "))
b=int(raw_input("b: "))
c=int(raw_input("c: "))
delt=b*b-4*a*c
x1=(-b-math.sqrt(delt))/(2*a)
x2=(-b+math.sqrt(delt))/(2*a)
print "x1={} , x2={}".format(x1,x2)


