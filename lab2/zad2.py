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

# print_csv_array(new_array)

# to do 6 point

# array_of_deleted = []
# for element in new_array:   
#     id = element.get()[0]
#     string = element.get()[1]
#     res = re.findall(r'\w+',string)
#     print(res)
#     for array_of_words in res:
#         for i in range(len(array_of_words)): 
#             word = array_of_words[i]
#             for j in range(len(word)):
#                 letter = ord(word[j])
#                 letter += 1
#                 print(letter)
#                 try:
#                     if letter == ord(word[j+1]):
#                         array_of_words.pop(i)
#                         array_of_deleted.append([id,word])
#                 except IndexError:
#                     pass
#     # print(res)

# print(array_of_deleted)

    # for element2 in res:
    #     for i in range(len(element2)):
    #         letter = int(element2[i])
    #         letter += 1
    #         if letter == int(element2[i+1]):
                
