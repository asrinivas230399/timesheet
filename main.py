from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/customer/edit")
async def get_customer_edit():
    return JSONResponse(content={"message": "Customer Edit Page - GET Request"})

@app.post("/customer/edit")
async def post_customer_edit(name: str = Form(...), email: str = Form(...)):
    # Here you would typically process the form data and update the customer information
    return JSONResponse(content={"message": f"Customer {name} with email {email} updated successfully!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)