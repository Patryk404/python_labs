with open('./patterns/1000_pattern.txt') as textFile:
    lines =[line.split() for line in textFile]

arr = []

for line in lines:
    for l in line:
        arr.append(list(l))


counter = 0
for i in range(0,len(arr)): 
    s=0
    while (s+2) < len(arr[i]) and (i+2)<len(arr):
        if arr[i][s] == 'A' and arr[i][s+1] =='B' and arr[i][s+2]=='C':
            if arr[i+1][s] == 'B' and arr[i+2][s]=='C':
                counter+=1 
        s+=1

print(counter)
 
def _hash(arr):
    suma = 0
    for i in range(0,len(arr)):
            suma+=ord(arr[i])
    return suma


def rabin_karp(pattern,arr,q):
    d=10
    for y in range(0,len(arr-2)):
        m = len(pattern)
        n = len(arr[y])
        p = 0
        t = 0
        h = 1
        for i in range(0,m-1):
            h= (h*d)%q

        for i in range(0,m):
            p = (d*p+ord(pattern[i]))%q
            t = (d*t+ord(arr[i]))%q 
        
        for i in range(0,n-m+1):
            if p==t:
                for j in range(0,m):
                    if arr[i+j] != pattern[j]:
                        break
                j+=1
                if j==m:
                    j=1
                    print("Pattern is found at position: " + str(i+1))
            if i < n-m:
                t = (d*(t-ord(arr[i])*h) + ord(arr[i+m])) % q
                if t<0:
                    t= t+q

    # print(pattern_hash)

# algorytm karpacza
# d = 256
 
# def search(pat, txt, q):





alg_karp(arr,['A','B','C']) 
# search('ABC',arr,q)s