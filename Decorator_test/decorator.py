import time


def print_addition(func):
    """
    Prints out the addition as it happens
    """

    def wrapper(a, b):
        print("1")
        for i in range(a + b - 1):
            time.sleep(0.1)
            print("+")
            print("1")

        print("=")
        return func(a, b)

    return wrapper


@print_addition
def add(a, b):
    return a + b


result = add(10, 12)
print(result)
