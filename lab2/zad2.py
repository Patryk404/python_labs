def get_id(csv_object):   
    tuple = csv_object.get()
    # print(tuple()[1])
    return tuple()[1]
class CsvObject:
    def __init__(self,id,val):
        self.id = id 
        self.val = val 
    def get(self):
        return {self.id, self.val}

f = open('zadanie2.csv')

arr = f.readlines()

# print(f.readlines()) 

# print(arr)
new_array = []
for element in arr:
    id = element.split(',')[0]
    val = element.split(',')[1] 
    object = CsvObject(id,val)
    if val != '\n':
        new_array.append(object)

new_array.sort(key=get_id)

print(new_array)
# for element in new_array:
