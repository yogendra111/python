# and - if first is false it'll returned otherwise both will be evaluated and returns the last truthy value
# or - if first is true it'll returned otherwise both will be evaluated and returns the last truthy value
''' print(2 and 3)  # return 3
print(2 or 3)  # return 2 '''

# List
''' list1 = ["hii", 123, "what's"]
list2 = ['For', 'Geeks']
list1.append(list2)
list1.insert(3, 12) # insert at position 3
list1.extend([8, 'Geeks', 'Always']) # insert all 3 ele in list1
# list1[-1] returns last element from last
list1.remove(123)
list1.pop()
for x in list1:
    print(x) '''

# Set
''' set1 = {"a", "b", "c"} # a set cannot have duplicate values and we cannot change its items
set1.add("d")
for x in set1:
    print(x) '''

# Dictionary
# with each item as a Pair
''' Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict) '''

# enumerated
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


'''
# Return Keywords – Return, Yield is used to return generator
# Return keyword
def fun():
    s = 0

    for x in range(10):
        s += x
    return s


print(fun())


# Yield Keyword
def fun():
    s = 0

    for x in range(10):
        s += x
        yield s


for i in fun():
    print(i)
'''