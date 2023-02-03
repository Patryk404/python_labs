L = [None] * 48
 
L[0] = 1
L[1] = 2 

for i in range(1,47):
    L[i+1] = L[i-1] + L[i]

print(L)
