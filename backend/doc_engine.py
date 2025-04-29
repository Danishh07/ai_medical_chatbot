import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load environment variables
load_dotenv()

# Get API key from environment
HF_API_KEY = os.getenv("API_KEY")

if not HF_API_KEY:
    raise ValueError("Hugging Face API key not found. Please add it to your .env file")

# Load documents from /data folder
documents = SimpleDirectoryReader("backend/data").load_data()

# Use Hugging Face Inference API instead of HuggingFaceLLM
llm = HuggingFaceInferenceAPI(
    model_name="HuggingFaceH4/zephyr-7b-beta",
    token=HF_API_KEY,
)

# Setup embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create vector store index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Set up query engine
query_engine = index.as_query_engine(llm=llm)

# Main query function
def query_documents(user_query: str) -> str:
    return str(query_engine.query(user_query))
