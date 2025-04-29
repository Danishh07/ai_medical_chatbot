import os
from dotenv import load_dotenv
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

HF_API_KEY = os.getenv("API_KEY")
if not HF_API_KEY:
    raise ValueError("Hugging Face API key not found. Please add it to your .env file")

# Use HuggingFaceInferenceAPI for hosted model
chat_llm = HuggingFaceInferenceAPI(
    model_name="HuggingFaceH4/zephyr-7b-beta",
    token=HF_API_KEY,
)

def chat_with_ai(user_message: str) -> str:
    system_prompt = (
        "You are an AI-powered **mental and physical health assistant**. "
        "Only provide answers related to health, wellness, symptoms, treatments, and mental wellbeing. "
        "If a user asks about non-health topics like cooking, technology, or entertainment, respond with: "
        "'I'm here to help with health-related questions. Please ask me something related to your health or wellbeing.' "
        "Keep responses concise and easy to understand. Keep greetings short. Focus on being helpful, friendly, and direct."
    )

    formatted_prompt = (
        f"<|system|>\n{system_prompt}\n"
        f"<|user|>\n{user_message}\n"
        f"<|assistant|>\n"
    )

    response = chat_llm.complete(formatted_prompt)
    
    return response.text.strip()



