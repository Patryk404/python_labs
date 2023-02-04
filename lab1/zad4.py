try:
    test_list = [1,2,3,4,5]
    print(test_list[5])
except IndexError:
    print("list is %s length" %(len(test_list)))

try:
    x = 1/0 
except ZeroDivisionError:
    print("You can't divide by 0")

try:
    print(y)
except NameError:
    print("y variable does not exist")
