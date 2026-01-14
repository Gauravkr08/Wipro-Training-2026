for i in range(1,21):
    print(i)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)

    from functools import reduce

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    even_square_sum = reduce(
        lambda total, value: total + value,
        map(lambda n: n ** 2,
            filter(lambda n: n % 2 == 0, data))
    )

    print(even_square_sum)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    final_list = list(
        map(lambda n: n ** 2,
            filter(lambda n: n % 2 == 0, numbers))
    )

    for index, value in enumerate(final_list):
        print(index, value)