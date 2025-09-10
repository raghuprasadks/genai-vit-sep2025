import cohere

class RAGModel:
    def __init__(self, cohere_api_key, chromadb_collection):
        self.cohere_api_key = cohere_api_key
        self.chromadb_collection = chromadb_collection
        self.cohere_client = cohere.Client(cohere_api_key)

    def generate_response(self, query):
        # Retrieve relevant documents from ChromaDB
        documents = self.retrieve_documents(query)
        
        # Generate a response using Cohere
        response = self.call_cohere_api(query, documents)
        
        return response

    def retrieve_documents(self, query, top_k=3):
        # Embed the query using Cohere
        query_emb = self.cohere_client.embed(texts=[query]).embeddings[0]
        # Query ChromaDB for similar documents
        results = self.chromadb_collection.query(
            query_embeddings=[query_emb],
            n_results=top_k
        )
        # Extract document texts
        docs = results['documents'][0] if results['documents'] else []
        return docs

    def call_cohere_api(self, query, documents):
        # Concatenate retrieved documents for context
        context = "\n".join(documents)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        # Generate response using Cohere's generate endpoint
        response = self.cohere_client.generate(
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        return response.generations[0].text.strip()