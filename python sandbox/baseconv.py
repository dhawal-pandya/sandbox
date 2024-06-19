def convert_to_base(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result if result else "0"


def main():
    tonumber = 36

    for number in range(1, tonumber):
        tobase = number

        for base in range(
            2,
            tobase + 1,
        ):
            if base < 2 or base > 36:
                print("Base should be between 2 and 36.")
                return

            result = convert_to_base(number, base)
            print(f"{result} is {number} in base {base}")

        print("")


if __name__ == "__main__":
    main()
