import streamlit as st
from rag import RAGModel
from pdf_upload import upload_pdf
from utils import extract_text_from_pdf, initialize_chromadb

def main():
    st.title("RAG Application with PDF Upload")
    
    # Initialize ChromaDB
    client,collection = initialize_chromadb()
    
    # PDF Upload Section
    st.header("Upload PDF File")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Process the uploaded PDF
        text = upload_pdf(uploaded_file)
        #st.write("Extracted Text:")
        #st.write(text)
        
        # Initialize RAG Model
        cohere_api_key="yGlhFfYaems7Qn25x5DYVa2eS4NiLz6Bzuh5aXyc"
        #rag_collection = db.get_or_create_collection(name="rag_collection")
        rag_model = RAGModel(cohere_api_key,collection)
        
        # User Input for Query
        user_query = st.text_input("Enter your query:")
        
        if st.button("Generate Response"):
            if user_query:
                response = rag_model.generate_response(user_query)
                st.write("Response:")
                st.write(response)
            else:
                st.warning("Please enter a query to generate a response.")
    
if __name__ == "__main__":
    main()