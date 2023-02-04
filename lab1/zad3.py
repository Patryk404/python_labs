import time 
L=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9]


start_time_iteration = time.time()
for x in L:
    print(x)
print("Iteration: \n")
print("--- %s seconds ---" %(time.time() - start_time_iteration))

start_time_cpp_solution = time.time()
for i in range(19):
    print(L[i])
print("Cpp solution: \n")
print("--- %s seconds ---" %(time.time() - start_time_cpp_solution))

