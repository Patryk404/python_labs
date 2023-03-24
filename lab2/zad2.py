import re

def get_id(csv_object):   
    arr = csv_object.get()
    if arr[0] == "id": 
        return 0
    else:
        return int(arr[0])   

def print_csv_array(array):
    for element in array:
        element.print() 


class CsvObject:
    def __init__(self,id,val):
        self.id = id 
        self.val = val 
    def get(self):
        return [self.id,self.val]
    def inc_id(self):
        id = int(self.id)
        id +=1
        self.id=id
    def print(self):
        print([self.id,self.val])
    def set_lower_leters(self):
        self.val = self.val.lower()

f = open('zadanie2.csv')

arr = f.readlines()

new_array = []
arr.pop(0)
for element in arr:
    id = int(element.split(',')[0])
    val = element.split(',')[1] 
    object = CsvObject(id,val)
    if val != '\n':
        new_array.append(object)

new_array.sort(key=get_id)


for i in range(len(new_array)):
    for j in range(len(new_array)):
        if (new_array[j].get())[0] == (new_array[j-1].get())[0]:
            (new_array[j]).inc_id() 
    new_array.sort(key=get_id)



for element in new_array:
    element.set_lower_leters()

array_to_delete=[] 

for element in new_array:   
    id = element.get()[0]
    string = element.get()[1]
    res = re.findall(r'\w+',string)
    for array_of_words in res:
        for i in range(len(array_of_words)-1): 
            letter = ord(array_of_words[i])
            letter += 1 
            if ord(array_of_words[i+1]) == letter:
                array_to_delete.append([id,array_of_words])
 

print(array_to_delete)

indexes = []
for element in array_to_delete:
    id = int(element[0])
    exist=False
    for index in indexes:
        if index == id:
            exist = True
    if not exist:
        indexes.append(id)


new_array_without_indexes = []


for object in new_array:
    id = object.get()[0]
    exist = False
    for index in indexes:
        if id == index:
            exist = True
    if exist == False:
        new_array_without_indexes.append(object)

f = open("zadanie2_finished.csv","w")

f.write("id,val\n")

for object in new_array_without_indexes:
    [id, val] = object.get()
    f.write(str(id) + ","+ str(val)+"\n") 

f.close()
