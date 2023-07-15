# Tuples - immutable - cant change

tuple1 = (1, 2, 3)
print(tuple1[0])

# tuple1[0] =  5
# print(tuple1)

list1 = [1, 2, 3]
list1[0] = 5
print(list1)


tuple1 = (1,)
print(isinstance(tuple1, tuple))

list1 = list(tuple1)
print(list1)


list1 = [1]
tuple1 = tuple(list1)
print(tuple1)