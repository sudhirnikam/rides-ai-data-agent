from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def pick_llm(level: str):
    """
    Pick the LLM based on the level of the question.
    """
    level = level.lower()
    if level == "easy":
        llm = ChatOpenAI(model_name="gpt-6-luna", temperature=1)
    elif level == "medium":
        llm = ChatOpenAI(model_name="gpt-5.6-terra", temperature=0)
    elif level == "hard":
        llm = ChatOpenAI(model_name="gpt-6-sol", temperature=0)
    else:
        raise ValueError(f"Invalid level: {level}. Must be one of 'easy', 'medium', or 'hard'.")
    
    return llm

if __name__ == "__main__":
    # Example usage
    try:
        llm = pick_llm("easy")
        print(f"Picked LLM: {llm.model_name}")
        print(llm.invoke("What is the capital of Switzerland?"))
    except ValueError as e:
        print(e)