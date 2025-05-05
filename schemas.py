from pydantic import BaseModel

class VideoBase(BaseModel):
    title: str
    views: int
    likes: int


class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True

