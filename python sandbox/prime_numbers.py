def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_in_binary(up_to):
    for i in range(2, up_to + 1):
        if is_prime(i):
            print(f"{i} in binary: {bin(i)[2:]}")


# Example: Print prime numbers in binary up to 20
primes_in_binary(20)
