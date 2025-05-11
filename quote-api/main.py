from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres-db:5432/quotes")

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class QuoteCreate(BaseModel):
    text: str

class QuoteResponse(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI(title="Quote API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/quotes", response_model=QuoteResponse)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    db_quote = Quote(text=quote.text)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

@app.get("/quotes", response_model=list[QuoteResponse])
def read_quotes(db: Session = Depends(get_db)):
    quotes = db.query(Quote).all()
    return quotes

@app.get("/health")
def health_check():
    return {"status": "healthy"} 