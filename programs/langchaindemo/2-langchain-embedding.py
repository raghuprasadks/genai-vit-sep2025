from langchain_community.embeddings import CohereEmbeddings
from langchain.llms import Cohere
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="../.env")  # Adjust path if needed
api_key = os.getenv("cohere_api_key")
#print(f"API Key: {api_key}")

# Initialize Cohere Embeddings
embeddings = CohereEmbeddings(cohere_api_key=api_key, user_agent="langchain_colab_example")

# Example documents
docs = ["This is a document about pineapples.", "This is a document about oranges."]

# Split documents if needed
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs_split = splitter.create_documents(docs)

# Create Chroma vector store
vectorstore = Chroma.from_documents(docs_split, embeddings)

# Initialize Cohere LLM
llm = Cohere(cohere_api_key=api_key)

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Ask a question
query = "Tell me about pineapples."
answer = qa_chain.run(query)
print("Answer:", answer)