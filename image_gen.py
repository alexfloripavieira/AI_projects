import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model="dall-e-3",
    prompt="Um leão do time avai fc de florianópolis SC em seu estadio ressacada ele no centro do campo e o estadio cheio com a torcida",
    n=1,
    size="1024x1024",
    quality="standard",
)

image_url = response.data[0].url
print(image_url)