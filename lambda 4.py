from functools import reduce
def sum_of_squares_of_even_numbers(numbers: list) -> int:
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_numbers = map(lambda x: x ** 2, even_numbers)
    return reduce(lambda x, y: x + y, squared_numbers)
input_data = [1, 2, 3, 4, 5]
result = sum_of_squares_of_even_numbers(input_data)
print(result)
