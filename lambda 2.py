def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda x: x % 2 == 0, numbers))
input_data = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(input_data)
print(result)
