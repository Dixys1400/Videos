from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas


router = APIRouter(prefix="/videos", tags=["videos"])




@router.get("/", response_model=list[schemas.Video])
def get_all(db: Session = Depends(get_db)):
    return crud.get_videos(db)

@router.post("/", response_model=schemas.Video)
def create(video: schemas.VideoCreate, db: Session = Depends(get_db)):
    return crud.create_video(db, video)

