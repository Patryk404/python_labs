import math
def f(x,a,b,c):
    return a*pow(x,2)+b*x+c


def sin(x):
    return math.sin(x)

def circle(x,y,r):
    if (pow(x,2) + pow(y,2)) < pow(r,2):
        return True
    else:
        return False 

