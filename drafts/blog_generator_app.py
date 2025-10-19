import streamlit as st
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from PIL import Image
import os
import io

# Load environment variables
load_dotenv()

# Set up API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize model
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Define the state
class BlogState(TypedDict):
    topic: str
    outline: str
    content: str

# Define functions
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

# Build graph
graph = StateGraph(BlogState)
graph.add_node("create_outline", create_outline)
graph.add_node("write_content", write_content)
graph.add_edge(START, "create_outline")
graph.add_edge("create_outline", "write_content")
graph.add_edge("write_content", END)

# Compile workflow
workflow = graph.compile()

# Streamlit UI
st.set_page_config(page_title="AI Blog Generator", page_icon="🧠", layout="wide")

st.title("🧠 AI Blog Generator using LangGraph + OpenAI")

# Input field
topic = st.text_input("Enter a blog topic:", placeholder="e.g. The Future of Artificial Intelligence in Everyday Life")

# Button
if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("Generating blog content... ⏳"):
            # Run the workflow
            initial_state = {"topic": topic}
            final_state = workflow.invoke(initial_state)

        # Display results
        st.success("✅ Blog generated successfully!")
        st.subheader("📝 Outline")
        st.write(final_state["outline"])
        st.subheader("📜 Blog Content")
        st.write(final_state["content"])

# Optional: Show workflow graph
st.markdown("### 🕸 Workflow Graph")
try:
    img_bytes = workflow.get_graph().draw_mermaid_png()
    image = Image.open(io.BytesIO(img_bytes))
    st.image(image, caption="LangGraph Workflow", use_container_width=True)
except Exception as e:
    st.warning(f"Could not render workflow graph: {e}")
