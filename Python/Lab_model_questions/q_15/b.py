#Write a function in python to count and display the total number of words
def ct():
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
    wrd = []
    for line in fh:
        count = count+1
        wrds = line.rstrip().split()
        wrd.append(len(wrds))
    print("The number of words in the given text file are: ", sum(wrd))
    
ct()