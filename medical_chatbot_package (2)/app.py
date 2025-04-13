import gradio as gr
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains.question_answering import load_qa_chain
from huggingface_hub import login
import os

# 🔐 Use environment variable for API token
login(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# 1. Load and split documents
loader = PyPDFLoader("sample.pdf")
pages = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
documents = text_splitter.split_documents(pages)

# 2. Embedding and vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embeddings)

# 3. Load LLM from Hugging Face
llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0.5, "max_length": 512}
)

# 4. Create retriever and memory
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 5. Chain for conversation
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# 6. Gradio chat interface
def chatbot_interface(query):
    result = qa({"question": query})
    return result["answer"]

chat_interface = gr.ChatInterface(fn=chatbot_interface, title="📄 Medical ChatBot")

# 7. Launch app
chat_interface.launch()
