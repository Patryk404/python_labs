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

class Circle: 
    a=0
    b=0
    r=0 
    def __init__(self,r,a,b):
        self.r = r
        self.a = a
        self.b = b

    def val(self,x,y):
        if (x-self.a)**2 + (y-self.b)**2 <= self.r**2:
            return 1
        else: 
            return 0

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
# def sin(x):
#     return math.sin(x)

# def circle(x,y,r):
#     if (pow(x,2) + pow(y,2)) < pow(r,2):
#         return True
#     else:
#         return False 


# def monte_carlo_f(x,y,a,b,c):
#     rectangle = x*y 
#     rectange_pass = 0
#     for i in range(0,60000):
#         rand_x = random.randint(0,x)
#         rand_y = random.randint(0,y)
#         if rand_y == f(rand_x,a,b,c):
#             rectange_pass += 1
#     print(rectange_pass)
#     one_shit = rectange_pass/rectangle


# # def monte_sin(x,y):

# # def monte_circle(x,y):


# monte_carlo_f(100,100,1,2,3)
