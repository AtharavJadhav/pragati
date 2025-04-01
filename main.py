# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv
import logging
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="News Article Chatbot API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY environment variable is not set")
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    max_tokens: Optional[int] = Field(default=500)

class ChatResponse(BaseModel):
    response: str
    
# Helper function to validate API key
def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("API key not configured")
        raise HTTPException(status_code=500, detail="API key not configured")
    return api_key

# Routes
@app.get("/")
def read_root():
    return {"message": "News Article Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, api_key: str = Depends(get_api_key)):
    try:
        logger.info(f"Received chat request with {len(request.messages)} messages")
        
        # Prepare the system message for news articles specialization
        system_message = {
            "role": "system",
            "content": """You are a specialized news article assistant. 
            Focus on providing accurate, concise information about current events, 
            historical news contexts, and journalistic analysis. 
            Cite sources when possible and maintain a balanced, informative tone."""
        }
        
        # Format messages for OpenAI API
        formatted_messages = [system_message]
        for msg in request.messages:
            formatted_messages.append({"role": msg.role, "content": msg.content})
        
        logger.info(f"Sending request to OpenAI with {len(formatted_messages)} messages")
        
        # Call OpenAI API using the client
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # Using a more widely available model
                messages=formatted_messages,
                max_tokens=request.max_tokens,
                temperature=0.7
            )
            
            # Extract and return response
            assistant_response = response.choices[0].message.content
            logger.info("Successfully received response from OpenAI")
            return ChatResponse(response=assistant_response)
            
        except Exception as e:
            logger.error(f"OpenAI API Error: {str(e)}")
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)