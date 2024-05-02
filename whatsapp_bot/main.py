import os


import requests
from fastapi import FastAPI, Depends, Form
from requests.auth import HTTPBasicAuth
from twilio.twiml.messaging_response import MessagingResponse

import models
from database import engine, SessionLocal
from models import AudioMessage, Photo
from exceptions import NoFaceDetectedError
from services.audio_service import AudioService
from services.image_service import ImageService

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return {"msg": "up & running"}


# Route for handling incoming WhatsApp messages
@app.post("/whatsapp")
async def whatsapp(From: str = Form(...), MediaUrl0: str = Form(...),
                   MediaContentType0: str = Form(...), db: SessionLocal = Depends(get_db)):
    # Get message details
    from_number = From
    media_type = MediaContentType0
    media_url = MediaUrl0

    if media_type == 'audio/ogg':
        # Convert audio to WAV format
        wav_audio = AudioService.convert_audio_to_wav(requests.get(media_url).content)
        # Create and add audio message to database
        audio_message = AudioMessage(user_id=from_number, audio_data=wav_audio)
        db.add(audio_message)
    elif media_type.startswith('image/'):
        # Check if there are faces in the photo
        if not ImageService.detect_faces(requests.get(media_url).content):
            raise NoFaceDetectedError("There are no faces on the photo")
        # Create and add photo to database
        photo = Photo(user_id=from_number, photo_data=requests.get(media_url).content)
        db.add(photo)

    db.commit()

    return {"message": "File saved"}, 200
