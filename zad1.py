code1 = "79-900"
code2 = "80-155"


def postcode_generator(first_code, last_code):
    first_code_int = int(first_code.replace("-", ""))
    last_code_int = int(last_code.replace("-", ""))
    code_list = []
    for x in range(first_code_int+1, last_code_int):
        new_code_str = str(x)
        new_code = "{}-{}".format(new_code_str[0:2], new_code_str[2:6])
        code_list.append(new_code)
    return code_list


generate = postcode_generator(code1, code2)
print(generate)
