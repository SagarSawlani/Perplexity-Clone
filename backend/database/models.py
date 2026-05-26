from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
import uuid
import enum
from datetime import datetime, timezone

Base = declarative_base()

class AuthProvider(enum.Enum):
  Github = "Github"
  Google = "Google"

class User(Base):

  __tablename__ = "users"

  id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
  email = Column(String, nullable=False)
  provider =  Column(Enum(AuthProvider), nullable=False)
  name = Column(String, nullable=False)
  conversations = relationship("Conversation", back_populates="user")
  messages = relationship("Message", back_populates="user")

class Conversation(Base):
  __tablename__ = "conversations"

  id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
  title = Column(String, nullable=False)
  slug = Column(String, nullable=False)
  userId = Column(String, ForeignKey("users.id") ,nullable=False)
  user = relationship("User", back_populates="conversations")
  messages = relationship("Message", back_populates="conversation")

class MessageRole(enum.Enum):
  User = "User"
  Assistant = "Assistant"

class Message(Base):
  
  __tablename__ = "messages"

  id = Column(Integer, primary_key=True, index=True)
  content = Column(String, nullable=False)
  role = Column(Enum(MessageRole), nullable=False)
  conversationId = Column(String, ForeignKey("conversations.id"), nullable=False)
  createdAt = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  userId = Column(String, ForeignKey("users.id"), nullable=False)
  user = relationship("User", back_populates="messages")
  conversation = relationship("Conversation", back_populates = "messages") 