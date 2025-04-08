from fastapi import APIRouter
from src.database.db_connection import database, connect_db, disconnect_db
from sqlalchemy import Table, Column, Integer, String

customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String)
)

router = APIRouter()

@router.on_event("startup")
async def startup():
    await connect_db()

@router.on_event("shutdown")
async def shutdown():
    await disconnect_db()

@router.get("/customers")
async def get_customers(skip: int = 0, limit: int = 10):
    query = customers.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

@router.post("/customers")
async def create_customer(name: str, email: str):
    query = customers.insert().values(name=name, email=email)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "name": name, "email": email}

@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    query = customers.select().where(customers.c.id == customer_id)
    return await database.fetch_one(query)

@router.put("/customers/{customer_id}")
async def update_customer(customer_id: int, name: str, email: str):
    query = customers.update().where(customers.c.id == customer_id).values(name=name, email=email)
    await database.execute(query)
    return {"message": f"Customer {customer_id} updated"}

@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    query = customers.delete().where(customers.c.id == customer_id)
    await database.execute(query)
    return {"message": f"Customer {customer_id} deleted"}