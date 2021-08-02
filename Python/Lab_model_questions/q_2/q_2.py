
dict = {}
try:
    inp = int(input("Enter a number "))
except:
    print("Invalid input")
    quit()
for i in range(inp+1):
    dict[i] = i*i
dict.pop(0)
print(dict)