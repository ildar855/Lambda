def square_numbers(numbers: list) -> list:
    return list(map(lambda x: x ** 2, numbers))
input_data = [1, 2, 3, 4, 5]
result = square_numbers(input_data)
print(result)
