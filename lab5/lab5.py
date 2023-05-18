with open('./patterns/1000_pattern.txt') as textFile:
    lines =[line.split() for line in textFile]

arr = []

for line in lines:
    for l in line:
        arr.append(list(l))


counter = 0
for i in range(0,len(arr)):
    s=0
    print(len(arr[i]))
    while (s+2) < len(arr[i]) and (i+2)<len(arr):
        print(s+2)
        if arr[i][s] == 'A' and arr[i][s+1] =='B' and arr[i][s+2]=='C':
            if arr[i+1][s] == 'B' and arr[i+2][s]=='C':
                counter+=1 
        s+=1

print(counter)