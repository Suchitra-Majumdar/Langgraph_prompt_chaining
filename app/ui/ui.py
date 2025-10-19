import streamlit as st
from PIL import Image
import io

def show_blog_ui(workflow):
    st.title("🧠 AI Blog Generator using LangGraph + OpenAI")
    topic = st.text_input("Enter a blog topic:", placeholder="e.g. The Future of Artificial Intelligence in Everyday Life")

    if st.button("Generate Blog"):
        if not topic.strip():
            st.warning("Please enter a topic first!")
        else:
            with st.spinner("Generating blog content... ⏳"):
                initial_state = {"topic": topic}
                final_state = workflow.invoke(initial_state)

            st.success("✅ Blog generated successfully!")
            st.subheader("📝 Outline")
            st.write(final_state["outline"])
            st.subheader("📜 Blog Content")
            st.write(final_state["content"])

            st.markdown("### 🕸 Workflow Graph")
            try:
                img_bytes = workflow.get_graph().draw_mermaid_png()
                image = Image.open(io.BytesIO(img_bytes))
                st.image(image, caption="LangGraph Workflow", use_container_width=True)
            except Exception as e:
                st.warning(f"Could not render workflow graph: {e}")
