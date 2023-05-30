coords = []
# algorytm siłowy 
class Backpack:
    def __init__(self,width,height): 
        self.width = int(width)
        self.height = int(height) 
        self.field = width*height
        self.space = 0
        self.value = 0 
        self.items = []
    def add_item(self,item):
        if self.space + item.field <= self.field:
            self.space += item.field
            self.value += item.value
            self.items.append(item)

class Item:
    def __init__(self,_id,width,height,value):
        self._id = _id
        self.width= int(width)
        self.height = int(height) 
        self.value = int(value)
        self.field = self.width*self.height


# greedy algorithm
# def  greedy()

with open("./data/packages20.txt",'r') as file:
    for line in file:
        line = line.strip().split('\n') 
        coords.append(line[0].split(','))


coords.pop(0)
coords.pop(0) 
items = []

for cord in coords:
    items.append(Item(cord[0],cord[1],cord[2],cord[3]))

backpack = Backpack(10,5)

# backpack.add_item()
# print(items)