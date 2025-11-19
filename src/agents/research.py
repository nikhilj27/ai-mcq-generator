from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = os.getenv("LLM")
hf_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def research_agent(topic: str) -> str:
    """A simple research agent that uses a HuggingFace LLM to generate research notes on a given topic."""
    endpoint = HuggingFaceEndpoint(
        repo_id=llm,
        max_new_tokens=500,
        temperature=0.7,
        huggingfacehub_api_token=hf_api_token,
        provider="auto"        
    )

    prompt = f"Research the following topic and provide detailed notes:\n\nTopic: {topic}\n\nNotes:"

    messages = [
        SystemMessage(content="You are a knowledgeable research assistant."),
        HumanMessage(content=prompt)
    ]

    response = ChatHuggingFace(llm=endpoint).invoke(messages)
    return response.content
    