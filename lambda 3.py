from functools import reduce
def multiply_numbers(numbers: list) -> int:
    return reduce(lambda x, y: x * y, numbers)
input_data = [1, 2, 3, 4]
result = multiply_numbers(input_data)
print(result)
