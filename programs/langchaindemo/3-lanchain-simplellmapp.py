import getpass
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../.env")  # Adjust path if needed

api_key = os.getenv("cohere_api_key")
os.environ["COHERE_API_KEY"] = api_key
"""
if not os.environ.get("COHERE_API_KEY"):
  os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key for Cohere: ")
"""

model = init_chat_model("command-r-plus", model_provider="cohere")


"""
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

transalation = model.invoke(messages)
print(transalation)
print(model.invoke("Hello, world!"))
response = model.invoke([{"role": "user", "content": "Hello"}])
print(response)

"""

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

prompt_response = model.invoke(prompt)
print(prompt_response.content)