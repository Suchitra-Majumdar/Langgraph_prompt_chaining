from langgraph.graph import StateGraph, START, END
from app.workflow.states import BlogState
from app.workflow.nodes import create_outline, write_content

def build_blog_workflow():
    graph = StateGraph(BlogState)
    graph.add_node("create_outline", create_outline)
    graph.add_node("write_content", write_content)
    graph.add_edge(START, "create_outline")
    graph.add_edge("create_outline", "write_content")
    graph.add_edge("write_content", END)
    return graph.compile()
