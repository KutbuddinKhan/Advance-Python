def remaining_fuel(initial, kilometers, ratio):
    return initial - kilometers * ratio


initial = 50
kilometers = 10
ratio = 2
print(remaining_fuel(initial, kilometers, ratio))
