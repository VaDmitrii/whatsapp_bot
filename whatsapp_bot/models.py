from sqlalchemy import Column, Integer, String
from sqlalchemy import LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AudioMessage(Base):
    __tablename__ = 'audio_messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    audio_data = Column(LargeBinary)


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    photo_data = Column(LargeBinary)
