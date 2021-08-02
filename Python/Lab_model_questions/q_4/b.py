#Write a function unique to find all the unique elements of a list
lst = ['rfd', 'rrfr', 'a', 'a', 'b']
def unique(lst):
    print("The unique elements in the list are: ")
    for element in lst:
        if lst.count(element) == 1:
            print("\t\t\t\t",element)

unique(lst)