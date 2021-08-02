tup = ()
for i in range(3):
    rn = int(input("Enter the roll number: "))
    nm = input("Enter name: ")
    mrks = int(input("Enter marks: "))
    tup += ((rn,nm,mrks),)
print(tup)

print(tuple('TutorialAICSIP'))
##If in a tuple, no trailing commas are present, the entered element is split into the individual characters
