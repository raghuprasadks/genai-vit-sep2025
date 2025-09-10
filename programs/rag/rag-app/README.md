# RAG Application with Cohere, ChromaDB, and Streamlit

This project is a Retrieval-Augmented Generation (RAG) application that utilizes Cohere for natural language processing and ChromaDB for efficient data retrieval. The application is built using Streamlit, allowing for an interactive web interface.

## Features

- Upload PDF files for processing and retrieval.
- Generate responses based on user input and retrieved data.
- Easy-to-use interface for interacting with the RAG model.

## Project Structure

```
rag-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── rag              # Contains RAG logic
│   │   └── __init__.py
│   ├── pdf_upload       # Handles PDF file uploads
│   │   └── __init__.py
│   └── utils            # Utility functions
│       └── __init__.py
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rag-app.git
   cd rag-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/main.py
   ```

## Usage Guidelines

- Navigate to the web interface provided by Streamlit.
- Use the PDF upload feature to upload documents that you want to process.
- Enter your queries to generate responses based on the uploaded content.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.