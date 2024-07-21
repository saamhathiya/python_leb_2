def check_element_in_list(element, my_list):
    return element in my_list

my_list = [1, 2, 3, 4, 5]
element_to_check = 3

if check_element_in_list(element_to_check, my_list):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
