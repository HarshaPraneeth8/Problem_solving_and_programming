'''
calculate the time difference between two times
'''
from datetime import datetime
string1='10:33:26'
string2='18:15:49'
Format='%H:%M:%S'
output=datetime.strptime(string2,Format)-datetime.strptime(string1,Format)
print(output)
