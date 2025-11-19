
from src.agents.research import research_agent
from src.agents.mcqgenerator import mcq_generator_agent

def run_pipeline():
    print("Running the pipeline...")
    
    topic = input("Enter a research topic: ")
    print(f"Researching topic: {topic}")
    
    research_data = research_agent(topic)
    print("Research done. Generating MCQs...")
    
    mcq_data = mcq_generator_agent(research_data)
    
    print(mcq_data)