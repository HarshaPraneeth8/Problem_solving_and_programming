nos = []
nossrtd = []
while True:
    num = input('Input a number:')
    if num == 'stop':
        break
    try:
        inp = float(num)
        inp.append(nos)
    except:
        continue
    i=0
    for element in nos:
        if nos[i]<nos[i+1] and nos[i]<nos[i-1]:
            nossrtd.append(nos)
            i=i+1

print(nos)
print(nossrtd)