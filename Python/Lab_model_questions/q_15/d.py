#Count the number of words that end with 'e' in a text file
def end_e():
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
            if wrd[-1] == 'e':
                lst.append(wrd)
            
    print("The number of words that end with 'e' are: ", len(lst))
end_e()
