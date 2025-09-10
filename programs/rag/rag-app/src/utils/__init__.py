import PyPDF2
import chromadb

def extract_text_from_pdf(pdf_file):
    # Extract text from a PDF file-like object
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def initialize_chromadb(persist_directory="chromadb_data"):
    # Initialize ChromaDB client and collection
    client = chromadb.Client(chromadb.config.Settings(persist_directory=persist_directory))
    collection = client.get_or_create_collection(name="rag_collection")
    return client, collection