
frst = input("Enter a fraction: ")
fr = (nm,dnm) = frst.split("/")
snd = input("Enter a fraction: ")
sn = (nm, dnm) = snd.split("/")
frn = []
scnd = []
for elements in fr:
    frn.append(int(elements))
frn = tuple(frn)
print(frn)
for elements in sn:
    scnd.append(int(elements))
scnd = tuple(scnd)
print(scnd)
mlt = tuple(elem_1 * elem_2 for elem_1, elem_2 in zip(frn, scnd))
print("Multiplication of the fractions: ", str(mlt[0])+"/"+str(mlt[1]))