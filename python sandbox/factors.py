import time
import math


def find_factors(number):
    factors = []
    square_root = math.ceil(math.sqrt(number))

    for i in range(1, (square_root) + 1):
        if number % i == 0:
            factors.append(i)
    factors.append(number)
    return factors


num = 999999999999999999
start_time = time.time()
result = find_factors(num)
end_time = time.time()
print(f"Factors of {num}: {result}")
elapsed_time_s = end_time - start_time
print(f"Elapsed time: {elapsed_time_s:.2f} seconds")
