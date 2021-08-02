#) Write a program to perform addition of two square matrices(With NumPy)
import numpy as np
  
r1 = 3
c1 = 3

print("Enter the entries of 3*3 matrix in a single line (separated by space): ")

entries1 = list(map(int, input().split()))        #input

matrix1 = np.array(entries1).reshape(r1, c1)      #Matrix 1
print(matrix1)
r2 = 3
c2 = 3

print("Enter the entries of the second  3*3 matrix in a single line (separated by space): ")
entries2 = list(map(int, input().split()))

matrix2 = np.array(entries2).reshape(r2, c2)   #Matrix 2
print(matrix2)

print("The added matrix is:")
print(matrix1*matrix2)         #Product of matrices
