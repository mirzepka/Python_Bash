import os
fileslist=[]
path="/home/michal"
fileslist.append(path)
while len(fileslist):
    pat=fileslist.pop()+'/'
    print(pat)
    for dire in os.listdir(pat):
        if '.' == dire[0]:
            continue
        if os.path.isdir(pat+dire):
            fileslist.append(pat+dire)


