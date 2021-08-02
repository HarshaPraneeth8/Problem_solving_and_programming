def add(x, y):
    #Add Functiom
    return x + y


def subtract(x, y):
    #Subtract Function
    return x - y


def multiply(x, y):
    #Multiply Function
    return x * y


def divide(x, y):
    #Divide Function
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

def exp(x,y):
    #square function
    return x**y

#Testing the code using print statements and commenting is not automated and easy
