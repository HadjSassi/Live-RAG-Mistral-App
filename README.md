# Steps To follow!
Still not dockerized, but you can run it locally.
```bash
python venv .venv
```

```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

# Overview

####  New File in documents/

     ↓ 
####  file_watcher 

     ↓ 
####  load & chunk text

     ↓ 
####  embed text

     ↓ 
####  store in Qdrant

     ↓
####  user prompt in CLI

     ↓
####  embed query → retrieve → send to Mistral → print response



# Step 1: Run Qdrant Locally

```docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant```

This runs Qdrant on:
   * localhost:6333 for HTTP
   * localhost:6334 for gRPC


# Step 2: Install Required Packages

```pip install watchdog langchain qdrant-client sentence-transformers```

# Step 3: Step 3: Create the Folder Structure
```
mkdir rag-live-app && cd rag-live-app
mkdir documents
touch main.py file_watcher.py embedder.py qdrant_client.py retriever.py
```

# Step 4: Qdrant Setup (```qdrant_utils.py```)

# Step 5: Embedding Setup (```embedder.py```)

# Step 6: File Watcher Setup (```file_watcher.py```)

# Step 7: Main Application Logic (```main.py```)

# Step 8: Run the Application

```python main.py```

Now we're just indexing files in the `documents/` folder. You can add text files to this folder, and they will be automatically processed and indexed.

** **
Now we will querying application.

🧠 What This Involves

📦 Components:

| Step | Component               | Tool                                      |
| ---- | ----------------------- | ----------------------------------------- |
| 1    | Load retriever          | `LangChain + QdrantRetriever`             |
| 2    | Ask user for a question | `input()` in CLI                          |
| 3    | Get relevant docs       | `retriever.get_relevant_documents(query)` |
| 4    | Construct prompt        | `stuff` or `map_reduce` using LangChain   |
| 5    | Call LLM                | `Mistral API (mistral-client)`            |
| 6    | Print answer            | CLI output                                |



# Step 9: Install necessary packages for querying

```pip install requests langchain qdrant-client```

# Step 10: You need to have an API key for Mistral. You can get it from [Mistral](https://mistral.ai/). Set it as an environment variable:


# Step 11: Create the Querying Script (```query.py```)