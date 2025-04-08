from fastapi import APIRouter, Form, HTTPException, Depends, UploadFile, File
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.schemas.customer import CustomerUpdate
from app.utils.image_handler import save_image

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customer/edit/{customer_id}")
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
