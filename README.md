# 535Questions

535Questions is a Q&A tool designed to help people search and understand the U.S. Constitution. It uses RAG (Retrieval-Augmented Generation) to back up its answers with actual text from the Constitution, amendments, and Supreme Court rulings so it isn't just making things up.

Right now, it's very much a work in progress. We're currently focused on building out the data pipeline to get the raw text cleaned up and into a vector database.

## What's working so far

- **PDF Scraper**: Extracts text straight from constitutional PDFs using `PyMuPDF`.
- **Text Chunker**: Recursively breaks down large documents into smaller, meaningful chunks that are easier to vectorize.
- **Embedder**: A generic wrapper class designed to plug into different LLM providers.
- **Gemini integration**: Hooked up Google's `google-genai` SDK to actually generate the text embeddings.

## How to run it locally

You'll need Python 3.10+ and a Gemini API key to run the current pipeline.

1. Clone the repo and install the requirements:

   ```bash
   git clone https://github.com/deepspraj/535Questions.git
   cd 535Questions
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the root folder and drop your API key in:

   ```env
   EMBEDDING_SERVICE_PROVIDER="gemini"
   EMBEDDING_MODEL="text-embedding-004"
   EMBEDDING_MODEL_API_KEY="your-gemini-key-here"
   ```

3. Run the script:
   ```bash
   python app.py
   ```
   _(Right now, `app.py` just tests scraping the PDF, chunking it, and embedding the first chunk to make sure the pipeline actually works.)_

## What's next (Roadmap)

- [ ] Add support for Groq, Claude, and OpenAI embeddings.
- [ ] Connect a real vector database (like ChromaDB or Pinecone).
- [ ] Write the actual retrieval and Q&A loop.
- [ ] Build a simple frontend or CLI for users to interact with.

> **Update:** A lot more things are coming on the way! Stay tuned. 🚀
