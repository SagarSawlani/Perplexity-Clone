from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from database.database import AsyncSession
from database import models
from sqlalchemy.orm import Session
router = APIRouter()

async def get_db():
  db = AsyncSession()
  try:
    yield db
  finally:
    await db.close()

# Signup
@router.post("/signup")
async def signup(db: Session = Depends(get_db)):
  return 

# Signin
@router.post("/signin")
async def signin():
  return
