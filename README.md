# DuckEE
A RAG system Rubber Duck

DuckEE: A Retrieval-Augmented Generation System
Overview
DuckEE is a Retrieval-Augmented Generation (RAG) system designed to assist users in querying information from a collection of documents, including text and PDF files. This program leverages state-of-the-art natural language processing models to provide informative responses, enhancing user interaction through text-to-speech capabilities.

Features
Query Input: Users can enter queries into a simple interface.
Retrieval System: DuckEE uses a combination of document loaders and embeddings to retrieve relevant information from a knowledge base built from user-provided text and PDF files.
Text-to-Speech: The application features a text-to-speech option that reads out responses aloud, making it more accessible.
Typing Effect: Responses are displayed with a typing effect, enhancing user experience.
Voice Toggle: Users can easily enable or disable voice output.
Technologies Used
Python: The primary programming language for building DuckEE.
LangChain: A framework for building applications with language models, enabling seamless document loading and retrieval.
PyQt5: A set of Python bindings for the Qt libraries, used for creating the graphical user interface (GUI).
pyttsx3: A text-to-speech conversion library in Python.
FAISS: A library for efficient similarity search and clustering of dense vectors.
Ollama: A server for hosting large language models, such as Mistral, that serve as the underlying generative model.
Installation
To run DuckEE on your local machine, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your_username/DuckEE.git
cd DuckEE
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Start the Ollama server:

bash
Copy code
ollama serve
Run the DuckEE application:

bash
Copy code
python gui.py
Usage
Input your query into the text box and press "Enter" or click the "Submit" button.
The system will retrieve relevant information and display it in the results box.
Optionally, enable the voice output to hear the response.
Contributions
Contributions to DuckEE are welcome! Feel free to submit issues, fork the repository, and create pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the developers of LangChain, PyQt5, and other libraries that made this project possible.
