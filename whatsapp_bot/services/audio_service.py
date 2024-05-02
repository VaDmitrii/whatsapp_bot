import io
from datetime import datetime

from pydub import AudioSegment


class AudioService:

    @staticmethod
    def convert_audio_to_wav(audio_data) -> bytes:
        try:
            # loading opus-format audio file
            ogg_audio = AudioSegment.from_file(io.BytesIO(audio_data), format="ogg")

            # convert to WAV format
            wav_data = io.BytesIO()
            ogg_audio.export(wav_data, format="wav")
            wav_data.seek(0)
            return wav_data.read()
        except Exception as e:
            print(f"Error converting audio {e}")
            return b''


