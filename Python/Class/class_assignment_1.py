inp=input("Enter the file name: ")
#Creating a file handle
try:
    fh=open(inp)
except:
    print("Invalid input")
    quit()

char=[]
count=0
rep=dict()
totwords=[]

for line in fh:
    count=count+1                                         
    wrds = line.rstrip().split()
    for wrd in wrds:
        totwords.append(wrd)
        if wrd not in rep:
            rep[wrd]=1
        else:
            rep[wrd]=rep[wrd]+1
        for chara in wrd:
            char.append(chara)


print("\nThe number of characters in the given text file is:", len(char))
print("The number of lines in the given text file are:",count)
print("The number of words in the given text file are: ",len(totwords),"\n")

for k,v in sorted(rep.items()):
    if v>1:
        #prints only the items that appeared more than once
        print(k, ":", v)

    

    

    
  




    
   


  

