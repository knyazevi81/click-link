from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from crud import get_target, create_target, delete_target
import schemas 
from .utils import generate_url, validate_url

route = APIRouter(prefix="/api", tags=["service"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@route.post("/create_target", response_model=schemas.Target | schemas.UrlError)
def create_target_url(target: schemas.TargetCreate, db: Session = Depends(get_db)):
    """
    (ссылка без организации)
    Роут для создания таргетной url_code, переходя по 
    https://clclk.ru/url_code
    информация о переходе будет сохраняться
    """
    while True:
        url_code: str = generate_url()

        if not validate_url(target.redirect_by):
            raise HTTPException(
                status_code=404,
                detail={
                    "status": "404",
                    "detail": "incorrectly specified redirectby"
                }
            )
                
        if not get_target(db=db, url=url_code):
            return create_target(db=db, url=url_code, target=target)


@route.delete("/delete_target", response_model=schemas.Target)
def delete_target_url(target: schemas.DeleteTarget, db: Session = Depends(get_db)):
    return delete_target(db=db, url_code=target.url)










    