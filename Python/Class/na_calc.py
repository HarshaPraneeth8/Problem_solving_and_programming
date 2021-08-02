d=float(input("Enter the diameter value: "))
l=float(input("Enter the lenth: "))

import op_fb 
print("The value of numerical aperture is: ", op_fb.n_a(d,l))
print("The acceptane angle is: ",op_fb.a_a(d,l))