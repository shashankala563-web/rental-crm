from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

# An APIRouter helps organize endpoints into logical groups (microservices).
router = APIRouter(
    prefix="/api/clients",  # All endpoints in this router will start with /api/clients
    tags=['Clients']      # Groups endpoints in the API docs
)

# --- Create a New Client ---
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ClientResponse)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Creates a new client in the database.
    """
    new_client = models.Client(**client.model_dump())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# --- Get All Clients ---
@router.get("/", response_model=List[schemas.ClientResponse])
def get_clients(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieves a list of all clients from the database.
    """
    clients = db.query(models.Client).offset(skip).limit(limit).all()
    return clients
