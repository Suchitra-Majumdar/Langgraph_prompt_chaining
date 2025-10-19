from workflow.states import BlogState
from langchain_openai import ChatOpenAI
from app.config.config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# Initialize model
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def create_outline(state: BlogState) -> BlogState:
    prompt = f"Create a detailed outline for a blog post about the topic: {state['topic']}"
    outline = model.invoke(prompt).content
    state["outline"] = outline
    return state

def write_content(state: BlogState) -> BlogState:
    prompt = (
        f"Write a detailed blog post based on the following outline and topic:\n\n"
        f"Topic: {state['topic']}\nOutline:\n{state['outline']}"
    )
    content = model.invoke(prompt).content
    state["content"] = content
    return state
