# 🧠 Ask-Huberman – RAG Chatbot for Podcast Insights

Ask-Huberman is a Retrieval-Augmented Generation (RAG) chatbot that lets users interact with *The Huberman Lab Podcast*. 
Let's be real, Andrew Huberman podacasts information apcked but lengthy and hard to retrieve informations from. That is why I have made a chat bot that is trained on 
his podcast, that answers questions based on what he has said said in his podcast.

---

## 📌 Features

- 🎙️ Transcribes entire YouTube episodes
- 📄 Converts transcripts into structured, searchable text
- 🧠 Uses Weaviate (vector database) to store and embed transcripts
- 🤖 Leverages Cohere API to answer user queries via RAG
- 🧪 Semantic search powered by text embeddings and grouped prompt tasks
- 🔄 Easily extendable to other podcasts or long-form audio content

---

## 💻 Tech Stack

- **Python**
- **Weaviate** – vector store for transcript embeddings
- **Cohere** – for RAG-powered question answering
- **YouTubeTranscriptAPI / pytube** – for pulling transcripts or audio

---

## 🛠️ How It Works

1. **Transcription**  
   Extracts audio from YouTube and transcribes using YouTubeTranscriptAPI.

2. **Data Structuring**  
   Converts the transcript into chunks and stores them as JSON.

3. **Vectorization & Storage**  
   Uses Weaviate to create vector embeddings for each chunk and stores them for fast semantic querying.

4. **Query + Generation (RAG)**  
   - User enters a natural language question  
   - The system performs a similarity search using Weaviate  
   - The top relevant chunks are passed into a prompt  
   - Cohere generates a grounded answer based only on those chunks

