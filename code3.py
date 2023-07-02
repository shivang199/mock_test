def get_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_list = get_even_numbers(input_list)
print(output_list)
