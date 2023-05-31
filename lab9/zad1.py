
import numpy as np
import itertools
import random
import multiprocessing

coords = []

class Backpack:
    def __init__(self,height,width): 
        self.width = int(width)
        self.height = int(height) 
        self.field = np.zeros((self.width,self.height))
        self.items = []
        self.value = 0 
    def add_item(self,item):
        item_width,item_height = item.height,item.width
        for w in range(self.width- item_width+1):
            if w+item_width> self.width + 1 :
                break
            for h in range(self.height - item_height+1):
                if h + item_height > self.height +1 :
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        #rotation
        item_width,item_height = item_height,item_width
        for w in range(self.width- item_width +1):
            if w+item_width> self.width :
                break
            for h in range(self.height - item_height+1 ):
                if h + item_height > self.height +1 :
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        return False
    def display_backpack(self):
        print(self.field)
    def get_value_of_backpack(self):
        return self.value
            

class Item:
    def __init__(self,_id,width,height,value):
        self._id = _id
        self.width= int(width)
        self.height = int(height) 
        self.value = int(value)
        self.density = self.value/(self.width*self.height)

def greedy_algorithm(backpack,items):
    temp_items = items
    temp_items.sort(key=lambda item: item.density,reverse = True)
    for item in temp_items:
        backpack.add_item(item) 

def eval(gene):
    if isinstance(gene[-1],int):
        return 0
    temp_backpack = Backpack(20,20)
    value = 0
    for item in gene: 
        temp_backpack.add_item(item)
    return temp_backpack.get_value_of_backpack()

def population_algorithm(items):
    p = 50 # population size
    pc = 0.2 # elite percentage
    pm = 0.01 # mutations
    ps = 0.05 # mutation severity
    population = []
    val = 0
    try:
        counter = 0
        while counter < 500:
            counter += 1
            # generate random population
            for i in range(p-len(population)):
                population.append(random.sample(items,k=len(items)))


            # multicore eval
            pool = multiprocessing.Pool()
            result = pool.map(eval, population)
            
            for i in range(len(population)):
                if not isinstance(population[i][-1], int):
                    population[i].append(result[i])
 
            # sort according to perceived value
            population.sort(key=lambda g: -g[-1])
            print (counter, population[0][-1])
 
            # breed
            for i in range(round(p - 2 * pc * p)):
                b = random.randint(0, pc * p - 1)
                c = random.randint(pc * p, p - 2)
                bc = []
                iter_b = 0
                iter_c = 0
                for j in range(len(items)):
                    # randomize gene mixing
                    mixer = random.randint(0,1)
                    if mixer:
                        while population[b][iter_b] in bc:
                            iter_b += 1
 
                        if iter_b <= len(items):
                            copy = population[b][iter_b]
                            bc.append(copy)
                        else:
                            copy = population[c][iter_c]
                            bc.append(copy)
                        
                    else:
                        while population[c][iter_c] in bc:
                            iter_c += 1
 
                        if iter_c <= len(items):
                            copy = population[c][iter_c]
                            bc.append(copy)
                        else:
                            copy = population[b][iter_b]
                            bc.append(copy)
 
                population.append(bc)
                #population[-1].append(eval(population[-1]))
                
            del population[round(pc * p):p]
 
            # mutate
            for i in range(round(pm * len(population))):
                # pick entity to mutate
                m = random.randint(0, len(population) - 1)
                for j in range(round(ps * len(items))):
                    # pick two genes to swap
                    m1 = random.randint(0, len(items) - 1)
                    m2 = random.randint(0, len(items) - 1)
                    
                    temp = population[m][m1]
                    population[m][m1] = population[m][m2]
                    population[m][m2] = temp
                    if isinstance(population[m][-1], int):
                        del population[m][-1]
                    # eval new genome
                    #population[m].append(eval(population[m]))
    except KeyboardInterrupt: 
        print(val)
        print(population[0])
        print(len(population[0]))
        print(len(population))


def brute_force_algorithm(backpack,items):
    max_val = 0
    print(len(items)-1)
    for subset in itertools.permutations(items,len(items)):
        temp_backpack = Backpack(backpack.height,backpack.width) 
        for item in subset:
            temp_backpack.add_item(item)
        val = temp_backpack.get_value_of_backpack()
        if val > max_val:
            max_val = val
    return max_val

with open("./data/packages20.txt",'r') as file:
    for line in file:
        line = line.strip().split('\n') 
        coords.append(line[0].split(','))


coords.pop(0)
coords.pop(0) 
items = []

for cord in coords:
    items.append(Item(cord[0],cord[1],cord[2],cord[3]))

backpack1 = Backpack(20,20)

greedy_algorithm(backpack1,items)
print(backpack1.get_value_of_backpack())

backpack2 = Backpack(10,5)
# brute_force_algorithm(backpack2,items)
population_algorithm(items)

# greedy(backpack,items)
# backpack = Backpack(10,5)

# backpack.add_item()
# print(items)