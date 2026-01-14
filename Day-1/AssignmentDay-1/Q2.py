data = [1, 2, 3, 4, 5, 6, 2, 4]

unique_even_numbers = [x for x in set(data) if x % 2 == 0]

print(unique_even_numbers)

data = [1, 2, 3, 4, 5, 6, 2, 4]

unique_even_numbers = {x for x in data if x % 2 == 0}

print(unique_even_numbers)

numbers = [1, 2, 3, 4, 5]

cube_dict = {x: x ** 3 for x in numbers}

print(cube_dict)