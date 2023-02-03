from time import 
length = 48
L = [None] * length
 
L[0] = 1
L[1] = 2

def unique(list1):
    unique_list = [] 
    
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
     

    return unique_list

for i in range(1,length - 1):
    L[i+1] = (L[i-1] + L[i])/(L[i] - L[i-1])

print(L)
mediana = (L[length/2] + L[(length/2)+1])/2
srednia = 0
for i in range(0,length ):
    srednia += L[i]


unique_values = unique(L);



for x in unique_values:
    counter = 0;
    for y in L:
        if y == x:
            counter+=1
   
    if counter == 1:
        print("Liczba " + str(x) + " jest unikatowa\n")
    else: 
       print("Liczba " + str(x) + " pojawia sie "+ str(counter)+ " razy\n")

print(unique(L))
srednia = srednia/length
print("mediana: " + str(mediana))
print("srednia: " + str(srednia))
