import chromadb
import cohere
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")  # Adjust path if needed

api_key = os.getenv("cohere_api_key")

def get_relevant_docs(collection, cohere_client, query, top_k=3):
    # Embed the query
    query_emb = cohere_client.embed(texts=[query]).embeddings[0]
    # Query ChromaDB for similar documents
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=top_k
    )
    docs = results['documents'][0] if results['documents'] else []
    return docs

def generate_answer(cohere_client, query, docs):
    context = "\n".join(docs)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = cohere_client.generate(
        prompt=prompt,
        max_tokens=256,
        temperature=0.5
    )
    return response.generations[0].text.strip()

def main():
    cohere_api_key = api_key
    cohere_client = cohere.Client(cohere_api_key)
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(name="rag_collection_pdfs")

    print("RAG Chatbot (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        docs = get_relevant_docs(collection, cohere_client, query)
        answer = generate_answer(cohere_client, query, docs)
        print("Bot:", answer)

if __name__ == "__main__":
    main()