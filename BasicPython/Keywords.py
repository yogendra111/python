# Python program to illustrate the modules
# import math
import keyword


def Main():
    print("In Main")
    print('list of keywords: ', keyword.kwlist)
    print('list of soft keywords: ', keyword.softkwlist)
    '''num = int(input('Enter a number: '))
    num = math.fabs(num)
    print('Absolute float', num)'''


if __name__ == '__main__':
    Main()
