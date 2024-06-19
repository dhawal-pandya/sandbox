import time


class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"

    def execute(self, operation):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise CircuitBreakerOpenError("Circuit is open")
        try:
            result = operation()
            self.reset()
            return result
        except Exception as e:
            self.failure_count += 1
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                self.last_failure_time = time.time()
                raise CircuitBreakerOpenError("Circuit is open")
            else:
                raise e

    def reset(self):
        self.failure_count = 0
        self.state = "CLOSED"


class CircuitBreakerOpenError(Exception):
    pass


# Example usage:
def dangerous_operation():
    # Simulate some operation that might fail
    raise ValueError("Something went wrong")


breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=10)

try:
    result = breaker.execute(dangerous_operation)
    print("Result:", result)
except CircuitBreakerOpenError:
    print("Circuit is open, operation failed.")
