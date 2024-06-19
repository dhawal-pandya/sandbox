import time
import math


def rate_limiter(limit):
    def decorator(func):
        last_called = {}

        def wrapper(id):
            current_time = (
                time.time() * 1000
            )  # the * 1000 is to convert to milliseconds

            # if the ID has not been called before
            if id not in last_called:
                last_called[id] = current_time
                return func(id)

            # if the ID has been called before
            time_since_last_call = current_time - last_called[id]
            if time_since_last_call < 1 / limit:
                return "Rate limit exceeded. Please try again later."
            last_called[id] = current_time
            return func(id)

        return wrapper

    return decorator


# Limit is 1 call within 200 milliseconds
@rate_limiter(1 / 200)
def return_pi(id):
    return math.pi
