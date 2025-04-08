import time
import asyncio
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

async def run_performance_test(endpoint: str, method: str = "GET", data: dict = None):
    start_time = time.time()
    if method == "GET":
        response = client.get(endpoint)
    elif method == "POST":
        response = client.post(endpoint, json=data)
    elif method == "PUT":
        response = client.put(endpoint, json=data)
    elif method == "DELETE":
        response = client.delete(endpoint)
    else:
        raise ValueError("Unsupported HTTP method")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Endpoint {endpoint} executed in {execution_time:.4f} seconds with status code {response.status_code}")
    # Measure page load time
    page_load_time = response.elapsed.total_seconds()
    print(f"Page load time for {endpoint}: {page_load_time:.4f} seconds")
    return execution_time, response.status_code, page_load_time

async def main():
    # Simulate user interactions
    await run_performance_test("/")
    await run_performance_test("/customers")
    await run_performance_test("/projects")
    await run_performance_test("/customers", method="POST", data={"name": "John Doe", "email": "john@example.com"})
    await run_performance_test("/projects", method="POST", data={"name": "New Project", "description": "Project description"})
    await run_performance_test("/customers/1", method="PUT", data={"name": "Jane Doe", "email": "jane@example.com"})
    await run_performance_test("/projects/1", method="PUT", data={"name": "Updated Project", "description": "Updated description"})
    await run_performance_test("/customers/1", method="DELETE")
    await run_performance_test("/projects/1", method="DELETE")

if __name__ == "__main__":
    asyncio.run(main())