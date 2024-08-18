from sqlalchemy.orm import Session

import models, schemas


def get_target(db: Session, url: str):
    return db.query(models.Target).filter(models.Target.url == url).first()


def get_targets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Target).offset(skip).limit(limit).all()


def create_target(db: Session, url_code: str, target: schemas.TargetCreate):
    db_target = models.Target(
        url = url_code,
        redirect_by = target.redirect_by,
        is_activate = True
    )
    db.add(db_target)
    db.commit()
    db.refresh(db_target)
    return db_target

def delete_target(db: Session, url_code: str):
    target = db.query(models.Target).filter(models.Target.url == url_code).first()

    if target:
        target.is_activate = False

        db.commit()
        db.refresh(target)
        return True
    
    return False



def create_log(db: Session, log: schemas.LogCreate, target_id: int):
    db_log = models.Log(**log.dict(), target_id=target_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log



