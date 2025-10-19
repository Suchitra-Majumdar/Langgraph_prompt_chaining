import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="F:\git_repos\langgraph_prompt_chaining\.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
