import functools

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

even2 = list(filter(lambda x: x % 2 + 1, fibonacci))
print(even2)

'''
    python 1 is True, 0 is False
'''


