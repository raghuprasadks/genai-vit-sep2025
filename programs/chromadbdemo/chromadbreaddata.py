import chromadb

# Connect to persistent ChromaDB store (default directory is 'chromadb')
client = chromadb.PersistentClient()

# Get the collection
collection = client.get_or_create_collection(name="rag_collection")

# Get all documents (by ids, if you know them)
results = collection.get()
print("All stored documents:")
print(results['documents'])

# Or, query for similar documents
query_results = collection.query(
    query_texts=["fruit"],  # Chroma will embed this for you
    n_results=2
)
print("Query results:")
print(query_results['documents'])