# Recursion

# Fibbonacci series
# 1, 1, 2, 3, 5, 8, 13

def fibonacci(position):
    if position >= 3:
        output = fibonacci(position - 1) + fibonacci(position - 2)
    else:
        output = 1
    return output

response = fibonacci(6)
print(response)
