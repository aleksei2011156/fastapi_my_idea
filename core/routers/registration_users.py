from fastapi import Depends, HTTPException
from app import app
from ..schemas import Registration
from sqlalchemy.orm import Session
from ..settings import get_db
from ..crud import create_user
import re


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/registration")
async def registration(user: Registration, db: Session = Depends(get_db)):
    """
    Registration user in information system

    Args:
        user (Registration): {login:str, email:str, password:str}
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Raises:
        HTTPException: {
            400: Email already registered
        }

    Returns:
        call create user
    """    
    db_user = 1
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db=db, user=user)
