from workflow.graph_builder import build_blog_workflow
from ui.ui import show_blog_ui

workflow = build_blog_workflow()
show_blog_ui(workflow)
