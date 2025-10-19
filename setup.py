from setuptools import setup, find_packages

setup(
    name="Prompt_Chaining_with_Langgraph",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipykernel",
        "langgraph",
        "langchain",
        "langchain-openai",
        "python-dotenv",
        "dotenv",
        "streamlit",
        "pillow",
            ],

    author="Suchitra Majumdar",
    description="Prompt_Chaining_with_Langgraph",
    python_requires=">=3.11",
)
