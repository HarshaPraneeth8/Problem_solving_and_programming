#Write a function in python to read the content from a text file line by line and display the same on screen
def read_line():
    inp = input("Enter the file name: ")
    try:
        fh = open(inp)
    except:
        print("Invalid input")
        quit()

    char = []
    count = 0
    rep = dict()
    totwords = []

    for line in fh:
        print(line)
read_line()
