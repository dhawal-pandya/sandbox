def base_repr_custom(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result if result else "0"


def divisible_by_three_in_base3(up_to):
    for i in range(3, up_to + 1, 3):
        base3_repr = base_repr_custom(i, 3)
        print(f"{i} in base 3: {base3_repr}")


# Example: Print numbers divisible by three in base 3 up to 20
divisible_by_three_in_base3(20)
