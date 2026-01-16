# Question2a
data = [1, 2, 3, 4, 5, 6, 2, 4]
squares_list = [i ** 2 for i in data]
print(squares_list)


# Question2b
even_set = {i for i in data if i % 2 == 0}
print(even_set)

# Question2c
cube = {x: x ** 3 for x in data}
print("cube dictionary",cube)