def sum(n):
    if n<=1:
        return n
    return n + sum(n-1)
print("The sum of 10 numbers is:",sum(10))