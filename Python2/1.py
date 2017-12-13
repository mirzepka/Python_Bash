import os

filename = "example.xml"
file1=open(filename,"r")
lines=file1.readlines()
file2 = open(filename+"_backUp", 'w')
lines=lines[0::2]
for line in lines: 
    file2.write(line)
file2.close()

