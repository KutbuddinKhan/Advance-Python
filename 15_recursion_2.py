# Iterative way to counting number
def count_to_num(num):
    for i in range(1, num + 1):
        print(i)

count_to_num(3)

# Recursion to counting number
def count_num(num):
    if num > 0:
        count_num(num - 1)
        print(num)
    
print("Recursion to find the number:")
count_num(3)