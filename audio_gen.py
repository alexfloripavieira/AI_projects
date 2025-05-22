import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input="Na ilha formosa, cheia de graça, o time da raça",
)

response.write_to_file("meu_audio.mp3")