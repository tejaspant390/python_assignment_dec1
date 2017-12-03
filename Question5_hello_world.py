#Program to repeat string 'n' times.

def string_multiply(string, repeat):
    return string * repeat


word = str(input('Enter the string: '))
num = int(input('Enter how many times you want to repeat string: '))
print('\n\n')
final_string = string_multiply(word, num)
print(final_string)
