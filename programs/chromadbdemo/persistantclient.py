import chromadb

client = chromadb.PersistentClient()

client.heartbeat()
collection = client.get_or_create_collection(name="rag_collection")

collection.add(
    ids=["id1", "id2"],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ])
results = collection.query(
    query_texts=["This is a query document about hawaii"],  # Chroma will embed this for you
    n_results=2  # how many results to return
)
print(results)