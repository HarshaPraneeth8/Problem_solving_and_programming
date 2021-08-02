#Write a function dups to find all the duplicates in a list
lst = ['rfd', 'rrfr', 'a', 'a', 'b']
def unique(lst):
    print("The unique elements in the list are: ")
    for element in lst:
        if lst.count(element) > 1:
            print("\t\t\t\t", element)
unique(lst)