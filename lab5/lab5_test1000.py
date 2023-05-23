with open('./patterns/1000_pattern.txt') as textFile: # 1000_pattern 
    lines =[line.split() for line in textFile]

arr = []

for line in lines:
    for l in line:
        arr.append(list(l))


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


print(naive(arr))
print(rabin_karp('ABC',arr))