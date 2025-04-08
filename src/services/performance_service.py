import time
from typing import Callable, Any


def simulate_data_access() -> None:
    """
    Simulate a data access operation for performance testing.
    """
    print("Simulating data access...")
    time.sleep(1)  # Simulate a delay in data access
    print("Data access simulation complete.")


def performance_test(func: Callable) -> Callable:
    """
    Decorator to measure the performance of a function.
    """
    async def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        # Log the performance test result
        with open("performance_log.txt", "a") as log_file:
            log_file.write(f"Function {func.__name__} executed in {execution_time:.4f} seconds\n")
        return result

    return wrapper
