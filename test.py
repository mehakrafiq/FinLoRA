# Check if MPS is available
import torch
print("MPS Available:", torch.backends.mps.is_available())

# Check if Together is available
from together import Together
import dotenv
config = dotenv.dotenv_values(".env")
client = Together(api_key=config["TOGETHER_API_KEY"])

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "What are some fun things to do in New York?"}]
)
print(response.choices[0].message.content)