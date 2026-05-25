from fastapi import FastAPI
from dotenv import load_dotenv

router = FastAPI()

# Signup
@router.post("/signup")
async def signup():
  return

# Signin
@router.post("/signin")
async def signin():
  return
