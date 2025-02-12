from openai import OpenAI

openai = OpenAI(
    api_key="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"
)

response = openai.images.generate(
    prompt="Baby tiger laying with human baby",
    n=1,
    size="512x512"
)

print(response.data[0].url)