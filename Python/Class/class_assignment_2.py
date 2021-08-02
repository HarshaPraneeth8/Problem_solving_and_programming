#Examples of beautiful idiomatic python

#1
import operator as op
import re
from fileinput import close
from unicodedata import name
greet="Hey guys: hp"

#non idiomatic
data=greet.strip()
data=greet.lower()
data=greet.replace(":","!")


#idiomatic
data=greet.strip().lower().replace(":","!")

##2

#Non-idiomatic
ns = []
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()
for line in fh:
    line = line.strip()
    #getting the numbers using regex and adding them to an empty list
    nos = re.findall('[0-9]+', line)
    if len(nos) != 0:
        ns = ns+nos
#cconverting the sstrings in the list to integers
ns = list(map(int, ns))
print(sum(ns))
fh.close()

#or the shortened version is
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid input")
    quit()


#Idiomatic

print(sum([int(nu) for nu in re.findall('[0-9]+', open(fname).read())]))


#3
# Non-idiomatic
for element in lst: print(element); print(len(lst))
#Idiomatic
for element in lst:
    print(element)
    print(len(lst))

#4
#Non-Idiomatic
def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
#Idiomatic
def apply_operation(left_operand, right_operand, operator):
    operator_mapper = {'+': op.add, '-': op.sub,
                   '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand,right_operand)

#5
#Non Idioamtic
for wrd in wrds:
    word[len(word)-2: ]
#Idiomatic
for wrd in wrds:
    word[-2: ]

#6
#Non idiiomatic
sm=0
for element in lst:
    sm=element+sm
print(sm)
#Idiomatic
print(sum(lst))

#7
#Non idiomatic
user_email = {}
for user in users_list:
    if user.email:
    user_email[user.name] = user.email
#Idiomatic
user_email = {user.name: user.email
              for user in users_list if user.email}

#8
#Non idiomatic
users_first_names = set()
for user in users:
    users_first_names.add(user.first_name)
#Idiomatic
users_first_names = {user.first_name for user in users}

#9
#Non Idiomatic
x="hello"
y="hello"
z="hello"
#Idiomatic
x=y=z="hello"

#10
#Non Idiomatic
x = "name"
y = "hello"
name=x
greet=y
#Idiomatic
x = "name"
y = "hello"
(x,y)=(name,greet)

#11
#non idiomatic
greet=["hello","ppl"]
x=""
for element in greet:
    x +=element
#Idiomatic
greet = ["hello", "ppl"]
x="".join(greet)

#12
name="hp"
#Non Idiomatic
if name:print ("hey",name)
#Idimatic
if name:
    print("hey",name)

#13 
#Non idiomatic
if name == 'Tom' or name == 'Dick' or name == 'Harry':
    print(name)
#Idiomatic
name="Dick"
if name in ("Tom","Dick","Harry"):
    print(name)

#14
#non idiomatic
tr = True
value = 0
if tr:
    value = 1
print(value)
#Idiomatic
tr = True
value = 1 if tr else 0
print(value)

#15
#Non idiomatic
my_container = ['Larry', 'Moe', 'Curly']
index = 0
for element in my_container:
    print('{} {}'.format(index, element))
    index += 1
#Idiomatic
my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
    print('{} {}'.format(index, element))
    
#16
#Non idiomatic
my_list = ['Larry', 'Moe', 'Curly']
index = 0
while index < len(my_list):
    print(my_list[index])
index += 1
#Idiomatic
my_list = ['Larry', 'Moe', 'Curly']
for element in my_list:
    print(element)

#17
#Non idiomatic
for element in lst:
    if element in lsts:
        print(element)
    if element not in lsts:
        print("Element not in list")
#Idiomatic
for element in lst:
    if element in lsts:
        print(element)
    else:
        print("Element not in list")

#18
#Non idiomatic
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
#Idiomatic
def f(a, L=None):
    if L is None:
    L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

#19
#Non-Idiomatic
def equal(a, b, c):
    result = False
    if a == b == c:
        result = True
        return result
#Idiomatic
def equal(a,b,c):
    return a==b==c

#20
#Non-Idiomatic
colors=["blue","black","red","orange","white"]
for color in range(len(colors)-1,-1,-1):
    print(colors[color])
#Idiomatic
for color in reversed(colors):
    print(color)