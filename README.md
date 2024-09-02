# PDFChat: Smart Assistant for PDF Documents

PDFChat is an AI-powered assistant that allows users to interact with and query PDF documents. Using advanced language models and vector databases, PDFChat processes and retrieves information from uploaded PDFs, providing concise and relevant answers to user queries.

## Features

- **PDF Processing**: Upload PDF files, extract text, and segment it into manageable chunks for efficient retrieval.
- **Vector Store**: Store document chunks in a vector database for fast and accurate retrieval using embeddings.
- **Smart Querying**: Query the uploaded PDF using natural language and receive concise answers powered by large language models (LLMs).
- **Conversational Memory**: Maintain context across multiple queries within a session for a more natural interaction.

## Project Structure

```plaintext
PDFChat/
│
├── app/
│   ├── vectordb/
│   ├── llms/
│   ├── constants.py
│   ├── pdf_processor.py
│   └── chatbot.py
├── output
├── main.py
├── .venv
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── runtime.txt
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/saivenkat2001/pdfchat.git
   cd pdfchat
   ```


2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv .venv
    source .venv/Scripts/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    python main.py
    ```

5. **Access the Application:**

    Once the application is running, it will open a web-based interface where you can upload PDFs and interact with the assistant.
    **Usage** 
    Upload a PDF: Use the interface to upload a PDF document.

    Ask Questions: Type in your question regarding the content of the PDF.

    Receive Answers: The assistant will provide a concise and accurate response based on the document content.
    

### Acknowledgments
LangChain: For providing the framework to easily build and deploy language model-powered applications.
Chroma: For the efficient and scalable vector database used in this project.
Gradio: For the simple and powerful UI framework that makes interacting with AI models easy.