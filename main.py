from fastapi import FastAPI
from routers import videos, filter_by_likes, filter_by_views
import models
from database import engine



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(videos.router)
app.include_router(filter_by_likes.router)
app.include_router(filter_by_views.router)


