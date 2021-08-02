#Write a function to find and display the occurence of the word 'the'
def ct_the():
    lst = []
    inp = input("Enter the file name: ")
    try:
        fh = open(inp)
    except:
        print("Invalid input")
        quit()
    for line in fh:
        wrds = line.rstrip().split()
        for wrd in wrds:
            if wrd == 'the'or wrd == 'The':
                lst.append(wrd)

    print("The number of words that are 'the' is: ", len(lst))
    #print("The words are:",*lst, sep = "\n\t\t")


ct_the()
