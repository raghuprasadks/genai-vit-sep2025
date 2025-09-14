#pip install -qU "langchain[cohere]"

import getpass
import os

if not os.environ.get("COHERE_API_KEY"):
  os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key for Cohere: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("command-r-plus", model_provider="cohere")

#model.invoke("Hello, world!")
print(model.invoke("Hello, world!"))