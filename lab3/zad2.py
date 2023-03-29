import math

class Circle:
    r = 0
    
    def __init__(self,r):
        self.r = r
    
    def calc_area(self):
        return math.pi*(self.r*self.r)

    def calc_circ(self):    
        return 2*math.pi*self.r


class Triangle:
    a = 0
    b = 0 
    c = 0 
    def __init__(self,a,b,c):
        if a+b > c and a+c > b and b+c > a: 
            self.a = a
            self.b = b 
            self.c = c 
        else:
            raise Exception("Can't create triangle with this edges")

    def calc_area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def calc_circ(self): 
        return self.a + self.b +self.c
        
    
class Square:
    a = 0
    def __init__(self,a):
        self.a = a
    def calc_area(self):
        return self.a*self.a
    def calc_circ(self):
        return 4*self.a            
    
