
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    
    try:
        
        api_key=os.getenv("API_KEY")
        
        if not api_key:
            raise ValueError("api key not found")
        llm = ChatGroq(
            groq_api_key=api_key, model="llama-3.1-8b-instant", temperature=0
        )
        
        return llm
    
    except Exception as e:
        print(e)
