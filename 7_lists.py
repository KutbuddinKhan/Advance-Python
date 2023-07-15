# Lists

a = [1, 2, 3, 4]
print(isinstance(a, list))

# append in list
a.append(5)
print(a)
print(a[0])

# insert in list
# first - position
# second - element
# a.insert(2, "TEXT")
# print(a)

# Reverse the list
# a.reverse()
# print(a)

# ascending order
# print("before sort", a)
# a.sort()
# print("after sort",a)


# pop element
last_element = a.pop()
print(last_element)

# a.clear()
# print(a)

print("Second:")
b = [1, 2]
# b = b * 5
print(b)

print("Add array")
c = [4, 5]
print(b + c)

# range
print("Range:")
a = [1, 2, 3, 4, 5, 6]
print(a[1: 5])
print(a[0: 3])
print(a[: 4])


print("Copy:")
a = [1, 2, 3, 4, 5]
# a2 = a
a2 = a.copy()
a2.append(9)
print(a2)
print(a)

