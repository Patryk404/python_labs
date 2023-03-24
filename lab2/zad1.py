 
arr = [] 
string = ""
changed_string = ""
for i in range(500,3000):
    if(i%7==0 and i%5!=0):
        arr.append(i)
 
for element in arr:
    string += str(element)


for i in range(len(string)): # we can use replace instead of this for
    if string[i] == "2" and string[i+1] == "1":
        changed_string +='X' 
        changed_string +='X'
    else:
        changed_string+=string[i]

print(string)
print(changed_string)