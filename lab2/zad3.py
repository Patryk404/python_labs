import re 
import time

print("Type Something: ")
text = input()

words = re.findall(r'\w+',text)

if len(words) != 1:
    print("You should pass only one word!") 
else:
    correct_word = ""
    text.lower()
    start_time = time.time() 
    file = open('SJP.txt')
    sjp = file.read().splitlines()
    for word in sjp:
        if word == text: 
            correct_word = word
    if len(correct_word):
        print("word correct with sjp")
        print("--- %s seconds ---" %(time.time() - start_time))
    else:
        print("word not correct with sjp")
        print("--- %s seconds ---" %(time.time() - start_time))