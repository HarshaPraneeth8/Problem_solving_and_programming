import math
def n_a(a,b):
    return (a)/(math.sqrt((a**2)+(4)*(b**2)))

def a_a(a,b):
    return math.degrees(math.asin(n_a(a,b))) 
