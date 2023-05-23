import time

def naive(arr):
    positions = []
    for i in range(0,len(arr)): 
        s=0
        while (s+2) < len(arr[i]) and (i+2)<len(arr):
            if arr[i][s] == 'A' and arr[i][s+1] =='B' and arr[i][s+2]=='C':
                if arr[i+1][s] == 'B' and arr[i+2][s]=='C':
                    positions.append({"y": i,"x":s})
            s+=1
    return positions

class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0 
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return ''.join(self.text[self.window_start:self.window_end])

def rabin_karp(word, arr):
    positions = []
    for i in range(0,len(arr)-2):

        rolling_hash = RollingHash(arr[i], len(word))
        word_hash = RollingHash(word, len(word))

        for j in range(len(arr[i]) - len(word) + 1):
            if rolling_hash.hash == word_hash.hash:
                if rolling_hash.window_text() == word: 
                    temp = [arr[i][j],arr[i+1][j],arr[i+2][j]]
                    letters = RollingHash(temp,len(temp))
                    if letters.hash == word_hash.hash:
                        if letters.window_text() == word:
                            positions.append({"y": i,"x": j})
            rolling_hash.move_window()

    return positions

with open('./patterns/1000_pattern.txt') as textFile: # 1000_pattern 
    lines =[line.split() for line in textFile]

arr_1000 = []
for line in lines:
    for l in line:
        arr_1000.append(list(l))

with open('./patterns/2000_pattern.txt') as textFile: # 2000_pattern 
    lines =[line.split() for line in textFile]

arr_2000 = []
for line in lines:
    for l in line:
        arr_2000.append(list(l))


with open('./patterns/3000_pattern.txt') as textFile: # 3000_pattern 
    lines =[line.split() for line in textFile]

arr_3000 = []
for line in lines:
    for l in line:
        arr_3000.append(list(l))

with open('./patterns/4000_pattern.txt') as textFile: # 4000_pattern 
    lines =[line.split() for line in textFile]

arr_4000 = []
for line in lines:
    for l in line:
        arr_4000.append(list(l))

with open('./patterns/5000_pattern.txt') as textFile: # 5000_pattern 
    lines =[line.split() for line in textFile]

arr_5000 = []
for line in lines:
    for l in line:
        arr_5000.append(list(l))

with open('./patterns/8000_pattern.txt') as textFile: # 8000_pattern 
    lines =[line.split() for line in textFile]

arr_8000 = []
for line in lines:
    for l in line:
        arr_8000.append(list(l))



if __name__ == "__main__":
    start_time = time.time()
    naive(arr_1000)
    end_time = time.time()
    print("1000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_1000))))
    end_time = time.time()
    print("1000 pattern rabin karp: "+str(end_time - start_time))
    
    
    start_time = time.time()
    naive(arr_2000)
    end_time = time.time() 
    print("2000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_2000))))
    end_time = time.time()
    print("2000 pattern rabin karp: "+str(end_time - start_time))
    

        
    start_time = time.time()
    naive(arr_3000)
    end_time = time.time() 
    print("3000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_3000))))
    end_time = time.time()
    print("3000 pattern rabin karp: "+str(end_time - start_time))

            
    start_time = time.time()
    naive(arr_4000)
    end_time = time.time() 
    print("4000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_4000))))
    end_time = time.time()
    print("4000 pattern rabin karp: "+str(end_time - start_time))

                
    start_time = time.time()
    naive(arr_5000)
    end_time = time.time() 
    print("5000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_5000))))
    end_time = time.time()
    print("5000 pattern rabin karp: "+str(end_time - start_time))

    start_time = time.time()
    naive(arr_8000)
    end_time = time.time() 
    print("8000 pattern naive: "+str(end_time - start_time))
    start_time = time.time()
    print("number of occurrences: "+ str(len(rabin_karp('ABC',arr_8000))))
    end_time = time.time()
    print("8000 pattern rabin karp: "+str(end_time - start_time))
    




    
    

    
    