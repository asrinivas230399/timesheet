import time
from typing import Callable, Any


def log_performance_metrics(process_time: float) -> None:
    """
    Log the performance metrics to a file.
    """
    with open("performance_log.txt", "a") as log_file:
        log_file.write(f"Processed in {process_time:.4f} seconds\n")
        if process_time > 1.0:  # Assuming 1 second is the threshold for performance degradation
            log_file.write(f"Performance degradation detected: {process_time:.4f} seconds\n")


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
        log_performance_metrics(execution_time)
        return result

    return wrapper
