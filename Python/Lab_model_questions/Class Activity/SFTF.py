 #Design a Python script to sort numbers specified in a text file 


with open('C:/Users/pavan/Desktop/python files/newfile.txt') as myfile:
    for line in myfile:
        print(sorted(map(int,line.split(','))))



'''

data = []
with open('C:/Users/pavan/Desktop/python files/sorting.txt') as myfile:
    for line in myfile:
        data.extend(map(int, line.split(',')))
        print(sorted(data))

'''
