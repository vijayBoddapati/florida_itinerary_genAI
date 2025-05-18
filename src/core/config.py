import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LLM_MODEL_PATH = os.getenv("LLM_MODEL_PATH", "models/llama-2-7b-chat.Q4_K_M.gguf")
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))