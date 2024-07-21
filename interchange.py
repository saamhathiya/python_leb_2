def interchange_first_last(input_list):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list

input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print(output_list)

output :-
![Screenshot 2024-07-21 214220](https://github.com/user-attachments/assets/c3a3fb2f-4000-42a5-ab8c-564b33177477)
