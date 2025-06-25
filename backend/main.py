from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import Base, SessionLocal, engine
from backend.models import User
from backend.security import verify_password

app = FastAPI()

# Ensure tables are created
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class LoginRequest(BaseModel):
    email: str
    password: str


@app.get("/ping")
async def ping():
    return JSONResponse(content={"status": "ok"})


@app.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        return JSONResponse(content={"status": "invalid credentials"})
    return JSONResponse(content={"status": "success"})
