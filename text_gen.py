import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = open("meu_audio.mp3", "rb")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
)

print(response.text)