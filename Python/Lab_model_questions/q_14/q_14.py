dict = {}
while True:
    num = input("Enter the name: ")
    if num == "done":
        break
    try:
        nm = str(num)
        nu = int(input("Enter the number: "))
        dict[nm] = nu
    except:
        continue
print(dict)
##(a)
#for k,v in dict.items():
    #print("Name: ",k)
    #print("Number: ",v,"\n")
##(b)
#dict['genius'] = '58641651246811'
#dict['someo'] = '87564'
#print(dict)
##(c)
#dict.pop('genius')
#print(dict)
##(d)
#dict['someo'] = '8756563421445864'
##(e)
#if 'genius' in dict.keys():
    #print("Name in dictionary")
#else:
    #print("Not in dictionary")
##(f)
#print(sorted(dict.items()))
