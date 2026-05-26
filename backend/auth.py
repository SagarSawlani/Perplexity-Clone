from fastapi import APIRouter
from dotenv import load_dotenv
from database.database import AsyncSession
router = APIRouter()

db = AsyncSession()

# Signup
@router.post("/signup")
async def signup()
  return 

# Signin
@router.post("/signin")
async def signin():
  return
