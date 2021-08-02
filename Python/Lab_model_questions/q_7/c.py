#Given a list of fractions as a tuple, return the one that is smallest in value.
fr = []
frn = []
frs = []
while True:
    num = input('Enter a fraction:')
    if num == 'stop':
        break
    #try:
    fr = (nm, dnm) = tuple(num.split("/"))
    frs.append(fr)
    for elements in fr:
        frn.append(int(fr[0])/int(fr[1]))
                
i = frn.index(min(frn))
if i == 0:
    print("Smallest fraction: ", frs[0][0] + "/" + frs[0][1])
if i>0:
    print("Smallest fraction: ", frs[i-1][0] + "/" + frs[i-1][1])
https://www.youtube.com/watch?v=6tNS--WetLI&t=6s
https: // www.youtube.com/watch?v = 6tNS--WetLI & t = 6s
https: // www.youtube.com/watch?v = 6tNS--WetLI & t = 6s
