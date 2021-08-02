#Take in numbers as input until “stop” is entered. Then split the numbers into three lists: one containing all the numbers,
# one containing all even values, and one containing all odd. 
# Print out all three lists, as well as each list’s sum and average. 
# Assume all input values are integers.
lsevn = []
lsodd = []
lsnu = []
while True:
    num = input('Input a number:')
    if num == 'stop':
        break
    try:
        inp = int(num)
        lsnu.append(inp)
    except:
        continue
    if inp%2 == 0:
            lsevn.append(inp)
    if inp%2 != 0:
        lsodd.append(inp)
print('\nAll numbers:', lsnu,'\nAverage of all nummbers:', sum(lsnu)/len(lsnu),'\nSum of all numbers:', sum(lsnu))
print('\nEven numbers:', lsevn, '\nAverage of even nummbers:',sum(lsevn)/len(lsevn), '\nSum of even numbers:', sum(lsevn))
print('\nOdd numbers:', lsodd, '\nAverage of odd nummbers:',sum(lsodd)/len(lsodd), '\nSum of odd numbers:', sum(lsodd))

