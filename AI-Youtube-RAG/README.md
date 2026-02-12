🏗 Architecture
User Input (YouTube URL)

↓
        
Transcript Extraction (youtube-transcript-api)

↓
        
Transcript Processing

↓
        
Text Chunking (RecursiveCharacterTextSplitter)

↓
        
Watsonx Embeddings

↓
        
FAISS Vector Store

↓
        
Retriever (Similarity Search)

↓
        
Watsonx Granite LLM

↓
        
Summary or Answer

↓
        
Gradio UI


🔬 RAG Pipeline Design

Embedding Model: ibm/slate-30m-english-rtrvr-v2

LLM: ibm/granite-3-2-8b-instruct

Vector Store: FAISS (in-memory)

Chunk Size: 200

Overlap: 20

Retrieval: Top-k similarity search (k=7)

Decoding: Greedy

This shows you understand system design — not just coding.

✅ Add Future Improvements Section

Persistent FAISS index

Multi-video indexing

Metadata filtering

Streaming responses

Docker containerization

Deployment on HuggingFace Spaces

Caching transcripts

Rate limiting
