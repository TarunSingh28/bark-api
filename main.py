
from bark import SAMPLE_RATE, generate_audio, preload_models
from fastapi import FastAPI
from pydantic import BaseModel
from scipy.io.wavfile import write as write_wav
from fastapi.responses import Response

app = FastAPI()

import os
os.environ["SUNO_OFFLOAD_CPU"] = ""
os.environ["SUNO_USE_SMALL_MODELS"] = "1"

# download and load all models
preload_models()

class TextInput(BaseModel):
    textInput: str

@app.post("/audio_utility")
async def audio_utility(text_input: TextInput):
    received_text = text_input.textInput
    print("Received text:", received_text)
    audio_file = generate_audio(received_text)
    
    file_name = "audio.wav"
    try:
        os.remove(file_name)
    except OSError:
        pass

    write_wav(file_name, SAMPLE_RATE, audio_file)

    with open(file_name, "rb") as file:
        audio_data = file.read()

    response = Response(content=audio_data, media_type="audio/wav")
    response.headers["Content-Disposition"] = 'attachment; filename="audio.wav"'

    return response
