nu = input("Enter the number of students:")
tup = []
for i in range(int(nu)):
    inp = input("Enter the email ids: ")
    tup.append(inp)
tup = tuple(tup)
usnm = ()
dmnnm = ()

for i in tup:
    lst = i.split("@")
    usnm += (lst[0],)
    dmnnm += (lst[1], )

print(tup)
print("The user names are:", usnm)
print("The domains are:", dmnnm)
