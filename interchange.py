def interchange_first_last(input_list):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list

input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print(output_list)
