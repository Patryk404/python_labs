import math
with open("./TSP.txt") as textFile:   
    for line in textFile:
        lines = [line.split() for line in textFile]

paths=[]
for i in range(0,len(lines)-1):
    x1 = float(lines[i][1])
    y1 = float(lines[i][2])
    x2 = float(lines[i+1][1])
    y2 = float(lines[i+1][2])
    d = math.sqrt((x1-x2)**2+(y1-y2)**2) 
    print(str(lines[i][0]+"-->"+lines[i+1][0]+": "+str(d)))

