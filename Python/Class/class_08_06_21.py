#example
#c=[39.2,36.5,37.3,38,37.8]
#c_f=list(map(lambda c:(((9/5)*(c))+32),c))
#for temp_f in c_f:
    #print(temp_f)

#lamdas in reduce()
from functools import reduce
#even_lst=[2,4,6,8,10,]
#pd=reduce(lambda x,y: x*y,even_lst)
#ad=reduce(lambda x,y:x+y,even_lst)
#ssq=reduce(lambda x,y: ((x)+ (y**2)), even_lst)+even_lst[0]
#print(ssq)

#Recursion
#def fctrl(n):
    #if n==0:
        #return 1
    #else:
        #return n*(fctrl(n-1))

#print(fctrl(997))

#write a recursive py fn that returns the sum of the first n integers using recursion

#def sm_n(n):
    #if n==0:
        #return 0
    #else:
        #return n + (sm_n(n-1))
#print(sm_n(10))