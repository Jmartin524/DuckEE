import os
import subprocess
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from PyQt5.QtWidgets import QApplication
from gui import RAGSystemApp  # Import the GUI class

# Start Ollama automatically when the program runs
def start_ollama():
    try:
        subprocess.Popen(["ollama", "serve"])
        print("Ollama has been started.")
    except Exception as e:
        print(f"Error starting Ollama: {e}")

# Function to load documents from the data directory
def load_documents():
    document_dir = './data'
    documents = []
    
    for root, _, files in os.walk(document_dir):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith(".txt"):
                loader = TextLoader(filepath)
            elif filepath.endswith(".pdf"):
                loader = PyPDFLoader(filepath)
            else:
                # Ignore unsupported file types like .DS_Store and .textClipping
                print(f"Unsupported file type: {filepath}")
                continue
            documents.extend(loader.load())

    # Use HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)

    # Load Mistral model
    llm = OllamaLLM(model="mistral")

    # Build QA chain with Retriever
    retriever = vector_store.as_retriever()
    return RetrievalQA.from_chain_type(llm, retriever=retriever)

# Start Ollama server
start_ollama()

# Load the retrieval-based QA system
qa_chain = load_documents()

# Create and start the GUI application
if __name__ == "__main__":
    app = QApplication([])
    window = RAGSystemApp(qa_chain)
    window.show()
    app.exec_()