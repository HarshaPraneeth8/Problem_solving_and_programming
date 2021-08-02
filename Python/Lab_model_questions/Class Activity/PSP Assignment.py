#Design a Python script to determine the difference in date for given two dates in YYYY:MM:DD format (0 <= YYYY <= 9999, 1 <= MM <= 12, 1 <= DD <= 31) following the leap year rules.



from datetime import datetime, date                                                  #We can only import date class from the datetime module

t1 = date(year = 2002, month = 6, day = 25)                                          #we can instantiate date objects from the date class. A date object represents a date (year, month and day).
t2 = date(year = 2021, month = 7, day = 14)                                          #Gives us the difference between t1 & t2
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2002, month = 6, day = 25, hour = 7, minute = 9, second = 33)   #The first three arguments year, month and day in the datetime() constructor are mandatory.
t5 = datetime(year = 2021, month = 7, day = 14, hour = 5, minute = 55, second = 13)
t6 = t4 - t5                                                                         #Gives us the difference between t4 & t5
print("t6 =", t6)

print("type of t3 =", type(t3))                                                      #Output(A timedelta object represents the difference between two dates or times.)
print("type of t6 =", type(t6))  
