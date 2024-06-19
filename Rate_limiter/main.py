from rate_limiter import return_pi
import time

# Test the rate limiter
print(return_pi("user1"))  # Output: 3.141592653589793
print(return_pi("user1"))  # Output: Rate limit exceeded. Please try again later.
print(return_pi("user2"))  # Output: 3.141592653589793
print(return_pi("user2"))  # Output: Rate limit exceeded. Please try again later.

time.sleep(0.2)  # Sleep for 100 milliseconds
print(return_pi("user1"))  # Output: 3.141592653589793
print(return_pi("user2"))  # Output: 3.141592653589793
