print("List 1")
i=0
ls1=[]
ls2 = []
while i<3:
    try:
        inp1 = float(input("Enter number: "))
    except:
        continue
    i=i+1
    ls1.append(inp1)
print("List 1 is: ", ls1)
print("List 2")
i=0
while i < 3:
    try:
        inp2 = float(input("Enter number: "))
    except:
        continue
    i = i+1
    ls2.append(inp2)
print("List 2 is: \n",ls2)
cmbnd = []
dups = []
def overlap(x,y):
    cmbnd = x + y
    for iter in cmbnd:
        if cmbnd.count(iter)>1 and iter not in dups:
            dups.append(iter)
    print("Overlap is: ",dups)
    print("Join is: ",cmbnd)
overlap(ls1,ls2)
