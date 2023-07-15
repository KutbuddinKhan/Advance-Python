# Dictionary - key value pairs
dict1 = {
    "name": "John",
    "age": 19,
    "profession": "Accounting", 
    5: 29
}
print(dict1["name"])
print(dict1["age"])
print(dict1["profession"])
print(dict1[5])

print("iterate each value of the dict")
# iterate each value of the dict
for key, value in dict1.items():
    print(f'{key} {value}')