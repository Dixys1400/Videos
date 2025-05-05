from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/videos/by-views", tags=["Views"])


@router.get("/", response_model=list[schemas.Video])
def filter_by_views(
        min: int = Query(0),
        max: int = Query(1_000_000_000),
        db: Session = Depends(get_db)
):
    return crud.get_videos(db, min_views=min, max_views=max)

