from fastapi import APIRouter
import databases
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)
metadata = MetaData()

projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

router = APIRouter()

@router.on_event("startup")
async def startup():
    await database.connect()

@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@router.get("/projects")
async def get_projects(skip: int = 0, limit: int = 10):
    query = projects.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

@router.post("/projects")
async def create_project(name: str, description: str):
    query = projects.insert().values(name=name, description=description)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "name": name, "description": description}

@router.get("/projects/{project_id}")
async def get_project(project_id: int):
    query = projects.select().where(projects.c.id == project_id)
    return await database.fetch_one(query)

@router.put("/projects/{project_id}")
async def update_project(project_id: int, name: str, description: str):
    query = projects.update().where(projects.c.id == project_id).values(name=name, description=description)
    await database.execute(query)
    return {"message": f"Project {project_id} updated"}

@router.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    query = projects.delete().where(projects.c.id == project_id)
    await database.execute(query)
    return {"message": f"Project {project_id} deleted"}