def evens_in_binary(up_to):
    for i in range(2, up_to + 1, 2):
        print(f"{i} in binary: {bin(i)[2:]}")


# Example: Print even numbers in binary up to 20
evens_in_binary(20)
