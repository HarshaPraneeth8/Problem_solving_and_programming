#Write a program that defines a matrix and prints(With NumPy)
import numpy as np
  
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(r, c)
print(matrix)
