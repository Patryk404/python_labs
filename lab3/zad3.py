import math
import random

accuracy = 100000

class F:
    a=0
    b=0
    c=0
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c 
    def val(self,x):
        return self.a*pow(x,2)+self.b*x+self.c


def monte_carlo_f(fobj,a,b):
    integral = 0.0
    for i in range(0,accuracy):
        rand_x = random.uniform(a,b)
        integral+=fobj.val(rand_x)
    
    ans = (b-a)/float(accuracy)*integral

    return ans

def monte_carlo_sin(a,b):
    integral = 0.0 
    for i in range(0,accuracy):
        rand_x = random.uniform(a,b)
        integral += math.sin(rand_x)
    
    ans = (b-a)/float(accuracy)*integral
    return ans


def monte_carlo_circle(r,b):
    integral = 0.0
    total = 0 
    area = 0
    for j in range(b):
        for i in range(0,accuracy):
            rand_x = random.uniform(-r,r)
            rand_y = random.uniform(-r,r)
            if rand_x**2 + rand_y**2 <= r**2:
                integral+=1
            total+=1
        area = (2 * r) **2 * integral / total
    return area 


function = F(2,2,2)


print(monte_carlo_f(function,1,2))
print(monte_carlo_sin(0,30))
print(monte_carlo_circle(20,10))