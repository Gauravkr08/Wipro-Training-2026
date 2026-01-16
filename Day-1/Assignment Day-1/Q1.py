# Question – Widely Used Built-in Functions & Lambda

#   Question 1a Uses range() to generate numbers from 1 to 20

for i in range(1,21):
    print(i)

#   Question1b Uses filter() with a lambda to select only even numbers

numbers=[1,2,3,4,5,6,7,8,9,10]

result=filter(lambda x:x%2==0,numbers)

print(list(result))

#   Question1c  Uses map() with a lambda to square the filtered numbers


numbers=[1,2,3,4,5,6,7,8,9,10]

result=map(lambda x:x*2,numbers)

print(list(result))


#Question1D   Uses reduce() to calculate the sum of squared even numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x + y,map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
)

print(result)

#   Question 1E   Uses enumerate() to print the index and value of the final result list

final_result = [1, 2, 3]

for index, value in enumerate(final_result):
    print(index, value)