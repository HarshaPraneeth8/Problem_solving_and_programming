#Write a program to perform multiplication of two square matrices(Without_NumPy)
r1 = 3
c1 = 3

matrix1 = []
print("Enter the entries of the fist matrix (The size of the matrix is 3 x 3):")

for i in range(r1):          # loop for row entries
    lst = []
    for j in range(c1):      # loop for column entries
        lst.append(int(input()))
    matrix1.append(lst)

for i in range(r1):
    for j in range(c1):
        print(matrix1[i][j], end=" ")
    print()
A = matrix1

r2 = 3
c2 = 3

matrix2 = []
print("Enter the entries of the second matrix rowwise:")


for i in range(r2):          # loop for row entries
    lst = []
    for j in range(c2):      # loop for column entries
        lst.append(int(input()))
    matrix2.append(lst)

#Printing matrix 2
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end=" ")
    print()
n = int(r1)
B = matrix2
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


for i in range(len(A)):  # Iterating through columns
    for j in range(len(A[0])):
                                        # Adding the same element in matrix A to matrix B
        result[i][j] = A[i][j] * B[i][j]
                                        # Here, same element means that the element at the same positions
print("The matrix product is:")
for r in result:
    print(r)
