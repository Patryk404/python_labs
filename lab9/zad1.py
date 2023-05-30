import numpy as np
import itertools

coords = []

class Backpack:
    def __init__(self,height,width): 
        self.width = int(width)
        self.height = int(height) 
        self.field = np.zeros((self.width,self.height))
        self.items = []
        self.value =0
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
    def get_value_of_items(self):
        return self.value
            

class Item:
    def __init__(self,_id,width,height,value):
        self._id = _id
        self.width= int(width)
        self.height = int(height) 
        self.value = int(value)


def greedy_algorithm(backpack,items):
    temp_items = items
    temp_items.sort(key=lambda item: item.value,reverse = True)
    for item in temp_items:
        backpack.add_item(item)

def brute_force_algorithm(backpack,items):
    max_val = 0
    print(len(items)-1)
    for subset in itertools.permutations(items,len(items)):
        temp_backpack = Backpack(backpack.height,backpack.width) 
        for item in subset:
            temp_backpack.add_item(item)
        val = temp_backpack.get_value_of_items()
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
print(backpack1.get_value_of_items())

backpack2 = Backpack(10,5)
brute_force_algorithm(backpack2,items)
# greedy(backpack,items)
# backpack = Backpack(10,5)

# backpack.add_item()
# print(items)