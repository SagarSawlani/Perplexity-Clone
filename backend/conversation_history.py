from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from database.database import session
import os

load_dotenv()

router = APIRouter()
db = session()

# Past convesations get
@router.get("/conversations")
async def get_conversations():
  return

# Past conversation get
@router.post("/conversation/{conversationId}")
async def get_conversation():
  return