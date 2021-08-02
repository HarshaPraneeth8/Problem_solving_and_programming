frst = input("Enter a fraction: ")
fr = (nm, dnm) = frst.split("/")
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
nm = list(frn)[0] * list(scnd)[1]
dnm = list(frn)[1] * list(scnd)[0]
print("Division of the fractions: ", str(nm)+"/"+str(dnm))
