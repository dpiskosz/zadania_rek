input_list = [2, 3, 7, 4, 9]
last_element = 10


def search_missing_numbers(in_list, last):
    output_list = []
    for x in range(1, last+1):
        if x not in in_list:
            output_list.append(x)
    return output_list


missing_numbers = search_missing_numbers(input_list, last_element)
print(missing_numbers)