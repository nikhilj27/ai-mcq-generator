from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = os.getenv("LLM")
hf_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def mcq_generator_agent(research_data: str):
    """An MCQ generator agent that uses a HuggingFace LLM to create multiple-choice questions from research data."""
    endpoint = HuggingFaceEndpoint(
        repo_id=llm,
        huggingfacehub_api_token=hf_api_token,
        max_new_tokens=500,
        temperature=0.7,
        provider="auto"
    )
    
    RESPONSE_JSON = {
        "1": {
            "mcq": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "correct_answer": "C"
        },
        "2": {
            "mcq": "Which planet is known as the Red Planet?",
            "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
            "correct_answer": "B"
        }
    }

    prompt = f"Based on the following research data, generate 5 multiple-choice questions with 4 options each and indicate the correct answer. Response should be in provided format {RESPONSE_JSON}:\n\nResearch Data:\n{research_data}\n\nMCQs:"
    
    messages = [
        SystemMessage(content="You are an expert MCQ generator."),
        HumanMessage(content=prompt)
    ]

    response = ChatHuggingFace(llm=endpoint).invoke(messages)
    return response.content