from fastapi import FastAPI, Form, HTTPException, Depends, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models
from app.schemas.customer import CustomerUpdate
from app.utils.image_handler import save_image

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="app/templates")

@app.get("/customer/edit/{customer_id}", response_class=HTMLResponse)
async def get_customer_edit(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return templates.TemplateResponse("customer_edit.html", {"request": {}, "customer": customer})

@app.post("/customer/edit/{customer_id}")
async def post_customer_edit(
    customer_id: int,
    customer_update: CustomerUpdate,
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Handle image upload
    image_path = None
    if image:
        image_path = save_image(image)

    try:
        # Update customer data
        customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")

        customer.name = customer_update.name
        customer.email = customer_update.email
        if image_path:
            customer.image_path = image_path

        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while updating the customer")

    return JSONResponse(content={"message": f"Customer {customer_update.name} with email {customer_update.email} updated successfully!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
