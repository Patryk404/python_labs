import time
from zad1 import Backpack
from zad1 import Item 
from zad1 import greedy_algorithm
from zad1 import population_algorithm
 
def coords_to_items(coords):
    items = []
    for cord in coords:
        items.append(Item(cord[0],cord[1],cord[2],cord[3]))
    return items

coords100 = []
coords500 = []
coords1000 = [] 
if __name__ =="__main__":
    with open("./data/packages100.txt","r") as file:
        for line in file: 
            line = line.strip().split('\n')
            coords100.append(line[0].split(','))
    coords100.pop(0)
    coords100.pop(0)
    items100 = coords_to_items(coords100)

    backpack100_1 = Backpack(10,10)
    backpack100_2 = Backpack(10,10)

    start_time = time.time()
    greedy_algorithm(backpack100_1,items100) 
    end_time = time.time()
    print("Greedy Algorithm for 100 Items Time to execute: " + str(end_time - start_time)) 
    print("Greedy Algorithm for 100 Items Value: "+ str(backpack100_1.get_value_of_backpack()))
    backpack100_1.display_backpack()
    
    start_time = time.time()
    optimal_set_of_items, value = population_algorithm(backpack100_2,items100,True)
    end_time = time.time()
    print("Population Algorithm for 100 Items Time to execute: " + str(end_time -start_time))
    print("Population Algorithm for 100 Items Value: " + str(value))
    backpack100_2.add_items(optimal_set_of_items)
    backpack100_2.display_backpack()

#####################################################################
    with open("./data/packages500.txt","r") as file:
        for line in file:
            line = line.strip().split('\n')
            coords500.append(line[0].split(','))
    coords500.pop(0)
    coords500.pop(0)
    items500 = coords_to_items(coords500) 

    backpack500_1 = Backpack(10,10)
    backpack500_2 = Backpack(10,10) 

    start_time = time.time()
    greedy_algorithm(backpack500_1,items500)
    end_time = time.time()
    print("Greedy Algorithm for 500 Items Value: "+ str(backpack500_1.get_value_of_backpack()))
    
    optimal_set_of_items, value = population_algorithm(backpack500_2,items500)
    print("Population Algorithm for 500 Items Value: "+str(value))

######################################################################     
    with open("./data/packages1000.txt","r") as file:
        for line in file:
            line = line.strip().split('\n')
            coords1000.append(line[0].split(','))
    coords1000.pop(0)
    coords1000.pop(0)
    items1000 = coords_to_items(coords1000)

    backpack1000_1 = Backpack(10,10)
    backpack1000_2 = Backpack(10,10) 

    greedy_algorithm(backpack1000_1,items1000)
    print("Greedy Algorithm for 1000 Items Value: "+ str(backpack1000_1.get_value_of_backpack()))
    
    optimal_set_of_items, value = population_algorithm(backpack1000_2,items1000)
    print("Population Algorithm for 1000 Items Value: "+str(value))
