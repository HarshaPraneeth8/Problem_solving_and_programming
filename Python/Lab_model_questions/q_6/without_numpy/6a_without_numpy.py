# Write a program that defines a matrix and prints(Without NumPy)
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
  
mtrx = [] #creating a list matrix
print("Enter the entries rowwise:")
  
# For user input
for i in range(r):            # Iterating through the row entries and appending it to the list lst
    lst = []                  # Stores one row at a time
    for iter in range(c):        # Appending all collumn entries to the lst
         lst.append(int(input()))
    mtrx.append(lst)          
  

for i in range(r):
    for iter in range(c):
        print(mtrx[i][iter],end = " ")   # For printing in the matrix format
    print()                              # Here, the end is not allowing to print a neew line character so, we use print()


