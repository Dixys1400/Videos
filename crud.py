from sqlalchemy.orm import Session
import models, schemas

def get_videos(db: Session, min_views=None, max_views=None, min_likes=None, max_likes=None, keyword=None):
    query = db.query(models.Video)

    if min_views is not None:
        query = query.filter(models.Video.views >= min_views)
    if max_views is not None:
        query = query.filter(models.Video.views <= max_views)
    if min_likes is not None:
        query = query.filter(models.Video.likes >= min_likes)
    if max_likes is not None:
        query = query.filter(models.Video.like <= max_likes)
    if keyword:
        query = query.filter(models.Video.title.ilike(f"%{keyword}%"))


    return query.all()


def create_video(db: Session, video: schemas.VideoCreate):
    db_video = models.Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video



