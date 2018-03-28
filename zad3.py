from decimal import Decimal

start_value = Decimal("2.0")
end_value = Decimal("5.5")
step_value = Decimal("0.5")


def generate_list(start, end, step):
    number_list = []
    while start <= end:
        number_list.append(start)
        start = start + step
    return number_list


new_list = generate_list(start_value, end_value, step_value)
print(new_list)
