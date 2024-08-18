from fastapi import FastAPI
import crud, models, schemas
from database import SessionLocal, engine
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from routes.service import route as service_route

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_app() -> FastAPI:
    """
    инициалиализация app, 
    """
    app = FastAPI(
        title="click-link api",
        version="0.1.1"
    )
    app.include_router(service_route)
    return app

app: FastAPI = create_app()


@app.post("/target/", response_model=schemas.Target)
def create_target(target: schemas.TargetCreate, db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_target(db=db, target=target)


@app.get("/target/", response_model=list[schemas.Target])
def get_targets(db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return crud.get_targets(db)


@app.post("/target/{target_id}/logs/", response_model=schemas.Log)
def create_item_for_user(
    target_id: int, log: schemas.LogCreate, db: Session = Depends(get_db)
):
    return crud.create_log(db=db, log=log, target_id=target_id)