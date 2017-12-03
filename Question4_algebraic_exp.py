#Program to verify algebraic square formula

def check_square_formula(a, b):
    if (a + b) ** 2 == pow(a, 2) + 2 * a * b + pow(b, 2):
        print("The formula (a+b)^2 = a^2 + 2ab + b^2 is valid for the value of a = {:d} and b = {:d}".format(a, b))


a = int(input('Enter the value for variable a : '))
b = int(input('Enter the value for variable b : '))
print('\n')
check_square_formula(a, b)