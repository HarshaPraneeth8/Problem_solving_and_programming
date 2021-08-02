# Tuples are immutable and they are defined using parentheses()
#student=("hp","nk","kb","yo","something") #tuple packing
#print(student[:-2])

#***Benefits of using a tuple compared to a list***

#(s1,s2,s3,s4,s5)=student #tuple unpacking

student=("chandu","ramesh","ramu","tarak","tejas")
student_1=("chandu","ramesh",("ramu","tarak"),"tejas")
(s1, s2, s3, s4, s5) = student_1  # tuple unpacking
print(student_1[2][0])


