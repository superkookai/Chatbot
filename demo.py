from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(
    api_key=os.getenv("OPENAI_API_SECRET_KEY")
)

response = openai.images.generate(
    prompt="Baby tiger laying with human baby",
    n=1,
    size="512x512"
)

print(response.data[0].url)