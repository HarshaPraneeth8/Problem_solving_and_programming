#Write a program to print each line of a file in reverse order
inp = input("Enter the file name: ")
lst = []
try:
    fh = open(inp)
    
except:
    print("Invalid file name")
    quit()
for line in reversed(fh.readlines()):
    print(line)

#(reversed(fh.readlines()).elements())

