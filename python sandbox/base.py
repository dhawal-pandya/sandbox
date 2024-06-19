def convert_to_base(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result if result else "0"


def print_number_in_bases(number):
    for base in range(2, number):
        print(f"{number} in base {base}: {convert_to_base(number, base)}")


# Example: Print number 5 in all bases up to 5
print_number_in_bases(10)
