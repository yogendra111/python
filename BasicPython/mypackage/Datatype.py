# Python program to illustrate datatype

print("Out of block")


def getint():
    num1 = int(input("Enter a Number: "))
    return num1


def evenodd(num1):
    if num1 % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


def main():
    print("In Main")
    # define a set and its elements
    myset = {"Geeks", "For", "Geeks"}
    print(myset)

    # creates a tuple which is immutable
    '''tup = ('Geeks', 'For', 'Geeks') 
	print(tup)'''

    # list and iteration
    '''students = ["Rahul", 10, 4.76]
	for x in students:
		print(x)'''
    '''num = getInt()
	evenOdd(num)'''

    # for loop
    '''for step in range(5):
    print(step)'''


# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    main()
