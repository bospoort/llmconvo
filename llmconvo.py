import logging
from fastapi import FastAPI, Query
import requests
from pydantic import BaseModel

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

class ConversationRequest(BaseModel):
    topic: str
    role1: str
    role2: str
    messages: int

@app.post("/start_conversation")
def start_conversation(req: ConversationRequest):
    logger.debug(f"Received request: {req}")
    conversation_log = []
    port: int = 11434
    
    msg = f"Let's discuss {req.topic}. You are {req.role1}, and I am {req.role2}."
    logger.debug(f"Initial message: {msg}")
    current_speaker = "llama3.2:1b"
    
    for _ in range(req.messages):
        response = requests.post(
            f"http://localhost:{port}/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": msg, "stream": False, "options": {"num_thread": 8, "num_ctx": 2024}}
        )
        logger.debug(f"Response: {response.json()}")
        
        if response.status_code == 200:
            msg = response.json().get("response", "")
            conversation_log.append({"speaker": f"LLM{current_speaker}", "message": msg})
            current_speaker = "deepseek-r1:1.5b" if current_speaker == "llama3.2:1b" else "llama3.2:1b"
        else:
            return {"error": f"Failed to reach {current_speaker} on port {port}"}
    
    return {"conversation": conversation_log}
