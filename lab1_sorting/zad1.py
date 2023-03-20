L = [88,33,32,4,12] 
def insertionsort(A):
    for i in range(len(A)):
        x = A[i]
        j = i-1
        while j>=0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x

insertionsort(L)

print(L)
        