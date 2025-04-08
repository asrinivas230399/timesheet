from fastapi import FastAPI
from routers import example_router, customer_router, project_router
import time
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn

app = FastAPI()

# Middleware for logging
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status: {response.status_code}")
        return response

# Middleware for performance monitoring
class PerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Processed in {process_time:.4f} seconds")
        return response

# Add middleware to the app
app.add_middleware(LoggingMiddleware)
app.add_middleware(PerformanceMiddleware)

# Include the example, customer, and project routers
app.include_router(example_router.router)
app.include_router(customer_router.router)
app.include_router(project_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
