# 🧠 CODEBASICS FAQs

The **LLM-Powered News Research Tool** is a **Streamlit-based** application that enables users to extract, process, and analyze news articles using **Google Generative AI (Gemini)**. It leverages **FAISS** for efficient document retrieval and **LangChain** for seamless integration of LLM-based embeddings and question-answering capabilities.
## ✨ Features

- ✅ Accepts CSV files as input for FAQs.
- ✅ Converts documents into vector embeddings using **HuggingFace InstructEmbeddings**.
- ✅ Utilizes **Google Generative AI (Gemini)** for processing and answering user queries.
- ✅ Stores processed embeddings in a **FAISS vector database**.
- ✅ Provides a user-friendly **Streamlit** interface for interaction.
- ✅ Retrieves relevant information efficiently from stored knowledge base.


## 🛠️ Technologies Used

- **Python 3.11+**
- **Streamlit** - Web UI framework
- **LangChain** - Document processing & Retrieval QA
- **FAISS** - Vector storage
- **Google Generative AI (Gemini)** - Embeddings & Q&A
- **HuggingFace InstructEmbeddings** - Embedding model
- **dotenv** - API key management
## 📦 Installation

### 🔹 Prerequisites

- Ensure you have **Python 3.11+** installed.
- Install **Poetry** for dependency management.

### 🔹 Steps to Install

#### 1️⃣ Clone the repository:

```sh
git clone https://github.com/your-repo/llm-project.git
cd llm-project
```

#### 2️⃣ Install dependencies using Poetry:

```sh
poetry install
```

#### 3️⃣ Set up environment variables:

Create a `.env` file and add your **Google API key**:

```sh
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

---

## 🚀 Usage

### 🏗️ Creating the Knowledge Base

Run the following command to process and store document embeddings:

```sh
poetry run python main.py
```

### 🎯 Running the Streamlit App

```sh
poetry run streamlit run main.py
```

Enter your **question** in the UI, and the app will retrieve the most relevant response from the knowledge base.

    


## Screenshots

![App Screenshot][def]

![App Screenshot][def2]

![App Screenshot][def3]

![App Screenshot][def4]



[def]: ./assets/codebasics2.png

[def2]: ./assets/codebasics3.png

[def3]: ./assets/codebasics4.png

[def4]: ./assets/codebasics5.png
