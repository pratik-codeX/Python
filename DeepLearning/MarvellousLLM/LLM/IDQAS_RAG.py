# =========================================================
# Marvellous Infosystems
# Project Name: Intelligent Document Question Answering System
# Using RAG and Large Language Models
# Author: Piyush Manohar Khairnar
# Date: 23/10/2026
# =========================================================

import streamlit as st
import PyPDF2
import faiss
import numpy as np
import requests

from sentence_transformers import SentenceTransformer

# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_text_from_pdf(pdf_file):
    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        st.error(f"Error while reading PDF: {e}")

    return text


# =========================================================
# TEXT CHUNKING
# =========================================================

def split_text_into_chunks(text, chunk_size=500, overlap=100):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between 0 and chunk_size - 1.")

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks


# =========================================================
# LOAD EMBEDDING MODEL
# =========================================================

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


# =========================================================
# CREATE FAISS VECTOR DATABASE
# =========================================================

def create_vector_database(chunks, embedding_model):
    if not chunks:
        raise ValueError("No text chunks available for embedding.")

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, embeddings


# =========================================================
# SEARCH RELEVANT TEXT CHUNKS
# =========================================================

def search_relevant_chunks(
    question,
    chunks,
    index,
    embedding_model,
    top_k=3
):
    if not chunks:
        return []

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    question_embedding = np.asarray(
        question_embedding,
        dtype=np.float32
    )

    top_k = min(top_k, len(chunks))

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    relevant_chunks = []

    for chunk_index in indices[0]:
        if 0 <= chunk_index < len(chunks):
            relevant_chunks.append(chunks[chunk_index])

    return relevant_chunks


# =========================================================
# GENERATE ANSWER USING LOCAL LLM THROUGH OLLAMA
# =========================================================

def ask_llm(question, context):
    prompt = f"""
You are an intelligent document question-answering assistant
created for Marvellous Infosystems.

Project:
Intelligent Document Question Answering System using RAG
and Large Language Models.

Instructions:
1. Answer using only the supplied context.
2. Do not introduce outside knowledge.
3. If the answer is not present in the context, say:
   "I could not find the answer in the uploaded PDF."
4. Give a clear and simple explanation.
5. Use bullet points when appropriate.

Context:
{context}

Question:
{question}

Answer:
"""

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        return result.get(
            "response",
            "No response was returned by the language model."
        )

    except requests.exceptions.ConnectionError:
        return (
            "Ollama is not running. Start Ollama and ensure "
            "the llama3 model is available."
        )

    except requests.exceptions.Timeout:
        return "The request timed out while waiting for Ollama."

    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {e}"

    except (ValueError, KeyError) as e:
        return f"Error processing the LLM response: {e}"


# =========================================================
# DISPLAY PROJECT FLOW
# =========================================================

def show_project_flow():
    st.markdown(
        """
        ### Complete Project Flow

        ```text
        Upload PDF
            |
            v
        Extract Text from PDF
            |
            v
        Split Text into Chunks
            |
            v
        Convert Chunks into Embeddings
            |
            v
        Store Embeddings in FAISS
            |
            v
        User Asks a Question
            |
            v
        Convert Question into Embedding
            |
            v
        Search for Similar Chunks
            |
            v
        Prepare Relevant Context
            |
            v
        Send Context and Question to LLM
            |
            v
        Generate Final Answer
        ```
        """
    )


# =========================================================
# STREAMLIT PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Marvellous Infosystems | Intelligent Document QA System",
    page_icon="📘",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #0f172a, #1e293b);
        color: white;
    }

    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #38bdf8;
        text-align: center;
        text-shadow: 2px 2px 5px black;
        margin-top: 10px;
    }

    .sub-title {
        font-size: 24px;
        font-weight: bold;
        color: #facc15;
        text-align: center;
        margin-bottom: 20px;
    }

    .brand-box {
        background: linear-gradient(to right, #1e3a8a, #2563eb);
        color: white;
        border-left: 8px solid #facc15;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
        font-size: 17px;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
        color: white;
    }

    h1, h2, h3 {
        color: #38bdf8 !important;
    }

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: #facc15;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #f8fafc;
        color: black;
    }

    .stSuccess {
        background-color: #14532d;
        color: white;
    }

    .footer {
        text-align: center;
        color: #cbd5e1;
        font-size: 15px;
        margin-top: 40px;
    }

    [data-testid="stToolbar"],
    #MainMenu,
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER SECTION
# =========================================================

st.markdown(
    '<div class="main-title">Marvellous Infosystems</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Intelligent Document Question Answering System
        using RAG and Large Language Models
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="brand-box">
        <b>Author:</b> Piyush Manohar Khairnar<br><br>
        <b>Date:</b> 23/10/2026<br><br>
        <b>Technologies:</b><br>
        Python, Streamlit, PyPDF2, Sentence Transformers,
        FAISS, Ollama, Llama3<br><br>
        <b>Tagline:</b><br>
        आम्ही Technical संस्कार करतो !!!
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.header("📘 Project Information")

    st.write(
        """
        This project demonstrates a RAG-based PDF
        question-answering system using a local LLM.
        """
    )

    st.subheader("Technologies Used")

    st.markdown(
        """
        - Python
        - Streamlit
        - PyPDF2
        - Sentence Transformers
        - FAISS
        - Ollama
        - Llama3
        """
    )

    st.subheader("Concepts Covered")

    st.markdown(
        """
        - PDF Processing
        - Text Chunking
        - Embeddings
        - Vector Database
        - Semantic Search
        - Retrieval-Augmented Generation
        - Large Language Models
        - Prompt Engineering
        """
    )

    st.subheader("Ollama Command")

    st.code("ollama run llama3", language="bash")


# =========================================================
# APPLICATION TABS
# =========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "Upload PDF",
        "Project Flow",
        "Technical Concepts"
    ]
)


# =========================================================
# TAB 1: PDF UPLOAD AND QUESTION ANSWERING
# =========================================================

with tab1:
    st.header("Upload PDF Document")

    uploaded_file = st.file_uploader(
        "Upload your PDF file here",
        type=["pdf"]
    )

    if uploaded_file is not None:
        st.success("PDF uploaded successfully!")

        with st.spinner("Loading embedding model..."):
            embedding_model = load_embedding_model()

        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)

        if not pdf_text.strip():
            st.error(
                "No readable text was found in the uploaded PDF."
            )

        else:
            st.subheader("Extracted Text Preview")

            st.text_area(
                "First 2000 characters from PDF",
                pdf_text[:2000],
                height=220
            )

            with st.spinner("Splitting text into chunks..."):
                chunks = split_text_into_chunks(
                    pdf_text,
                    chunk_size=500,
                    overlap=100
                )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Characters",
                    len(pdf_text)
                )

            with col2:
                st.metric(
                    "Total Chunks",
                    len(chunks)
                )

            with col3:
                st.metric(
                    "Chunk Size",
                    "500 characters"
                )

            try:
                with st.spinner(
                    "Creating embeddings and FAISS vector database..."
                ):
                    index, embeddings = create_vector_database(
                        chunks,
                        embedding_model
                    )

                st.success(
                    "Vector database created successfully!"
                )

                st.subheader(
                    "Ask a Question About the Uploaded PDF"
                )

                question = st.text_input(
                    "Enter your question",
                    key="pdf_question"
                )

                if question.strip():
                    with st.spinner(
                        "Searching for relevant content..."
                    ):
                        relevant_chunks = search_relevant_chunks(
                            question,
                            chunks,
                            index,
                            embedding_model,
                            top_k=3
                        )

                    context = "\n\n".join(relevant_chunks)

                    st.subheader("Retrieved Relevant Context")

                    with st.expander(
                        "Click here to view retrieved context"
                    ):
                        st.write(context)

                    with st.spinner(
                        "Generating answer using the local LLM..."
                    ):
                        answer = ask_llm(
                            question,
                            context
                        )

                    st.subheader("Generated Answer")
                    st.success(answer)

            except Exception as e:
                st.error(
                    f"An error occurred while processing the PDF: {e}"
                )


# =========================================================
# TAB 2: PROJECT FLOW
# =========================================================

with tab2:
    st.header("RAG Architecture Flow")
    show_project_flow()


# =========================================================
# TAB 3: TECHNICAL CONCEPTS
# =========================================================

with tab3:
    st.header("Technical Concepts Used")

    st.markdown(
        """
        ### 1. PDF Processing

        PyPDF2 extracts readable text from PDF pages.

        ### 2. Text Chunking

        Large documents are divided into smaller,
        overlapping text chunks.

        ### 3. Embeddings

        Sentence Transformers convert text chunks
        into numerical vectors.

        ### 4. Vector Database

        FAISS stores vectors and performs similarity searches.

        ### 5. Semantic Search

        The user's question is converted into an embedding
        and compared with document chunk embeddings.

        ### 6. Retrieval-Augmented Generation (RAG)

        Relevant document content is retrieved before
        the language model generates an answer.

        ### 7. Large Language Model (LLM)

        Llama3, running locally through Ollama,
        generates the final response.

        ### 8. Prompt Engineering

        The retrieved context and user question are
        combined into a structured prompt.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
   
    <div class="footer">
        <hr>
        <b>Marvellous Infosystems</b><br>
        आम्ही Technical संस्कार करतो !!!<br>
        Project developed by Piyush Manohar Khairnar
        | Date: 23/10/2026
    </div>
    """,
    unsafe_allow_html=True
)