from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from database import SessionLocal
from crud import get_target, create_target
import schemas 
from .utils import generate_url, validate_url

route = APIRouter(tags=["target"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@route.get("/{url_code}")
def redirect_to_target_url(request: Request, db: Session = Depends(get_db)):
    user_agent = request.headers.get("user-agent")

    return {"user-agent": user_agent}


#@route.get("/{company}/{url_code}")
#def redirect_to_company_target_url()
#    pass
    