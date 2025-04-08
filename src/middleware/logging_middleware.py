import time
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status: {response.status_code}")
        return response

class PerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Processed in {process_time:.4f} seconds")
        # Log the performance metrics
        with open("performance_log.txt", "a") as log_file:
            log_file.write(f"Processed in {process_time:.4f} seconds\n")
            if process_time > 1.0:  # Assuming 1 second is the threshold for performance degradation
                log_file.write(f"Performance degradation detected: {process_time:.4f} seconds\n")
        return response