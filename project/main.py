from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customer/edit/{customer_id}")
async def get_customer_edit(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return JSONResponse(content={"name": customer.name, "email": customer.email})

@app.post("/customer/edit")
async def post_customer_edit(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    # Here you would typically process the form data and update the customer information
    # For example, find the customer by ID and update their details
    return JSONResponse(content={"message": f"Customer {name} with email {email} updated successfully!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
