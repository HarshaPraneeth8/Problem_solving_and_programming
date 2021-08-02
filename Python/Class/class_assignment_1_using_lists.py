inp = input("Enter the file name: ")
#Creating a file handle
try:
    fh = open(inp)
    
except:
    print("Invalid input")
    quit()
#Defining 
char = []
count = 0
totwords = []
i = 0
lst = []
lsts = []
nos = []
nlst = []
nnlst = []

#Getting the line count and creating a list with all the words
for line in fh:
    #count for lines
    count = count+1
    for chars in line:
        #count for characters(Including spaces)
        char.append(chars)
    wrds = line.rstrip().split()
    for wrd in wrds:
        #count for words
        totwords.append(wrd)
        

#Creating a list with non repeated words
for ele in totwords:
    if ele not in nlst:
        nlst.append(ele)

#For an element x of the non repeating list, finding its first appearance
#in the total list and finding the number of times it appeared on the total list
for ele in nlst:
    xstr=nlst[i]
    nnlst.append(xstr+": "+ str(totwords.count(totwords[totwords.index(xstr)])))
    i=i+1

#Output
print("\nThe number of words in the given file are:",len(totwords))
print("The number of lines in the given file are:",count)
print("The number of characters in the given file are:",len(char),"\n")
print("The word repitions in the given file are:")

#to print only the elements that appeared more than once in the text file
for item in nnlst:
    if int(item[-1]) > 1:
        print(item)
    
      





