# 🧠 AI Blog Generator (LangGraph + Streamlit + OpenAI)

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-yes-green)](https://streamlit.io/)  

An **interactive AI-powered blog generator** that leverages **LangGraph** and **OpenAI's GPT models** to create detailed blog outlines and full-length blog content based on a user-provided topic. Built as a **Streamlit web app** for simplicity and interactivity.

---

## 🔹 Features

- **Generate Blog Outlines**: Automatically creates a detailed outline for your chosen topic.  
- **Generate Full Blog Content**: Produces complete blog posts based on the generated outline.  
- **Interactive Web UI**: Streamlit interface for easy input and output.  
- **Workflow Visualization**: Displays the LangGraph workflow as a graph.  
- **Modular Design**: Easily extendable for more states, custom prompts, or additional AI functions.

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **LangGraph** – for defining AI workflow/state graphs  
- **LangChain + OpenAI** – GPT-3.5 for content generation  
- **Streamlit** – interactive web app  
- **dotenv** – manage API keys securely  
- **Pillow** – render workflow graph images  

---

## 📁 Project Structure
ai_blog_generator/
│
├── .env # OpenAI API key
├── .gitignore # Ignore virtual env, cache, secrets
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── app/
│ ├── blog_generator_app.py # Main Streamlit app
│ ├── workflow/
│ │ ├── blog_state.py # Blog state and AI functions
│ │ └── blog_graph.py # LangGraph workflow setup
│ └── utils/
│ └── helpers.py # Optional utility functions
│
└── assets/ # Images, logos, or static files


---

## ⚡ Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/Suchitra-Majumdar/Langgraph_prompt_chaining.git
cd Langgraph_prompt_chaining.git


Create a virtual environment (Conda or venv recommended)

conda create -n ai_blog python=3.10
conda activate ai_blog


Install dependencies

pip install -r requirements.txt


Add your OpenAI API key
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here


Run the Streamlit app

streamlit run app/blog_generator_app.py


The app will open in your browser at http://localhost:8501.

🖥️ Usage

Enter your blog topic in the text input box.

Click Generate Blog.

The app will display:

A detailed outline of your blog.

The complete blog content.

A visual LangGraph workflow showing the AI process.

🔧 Customization

Modify prompts in app/workflow/blog_state.py to fine-tune the AI output.

Add new nodes or states in app/workflow/blog_graph.py to extend the workflow.

Use app/utils/helpers.py for text formatting, logging, or streaming outputs.

⚠️ Important Notes

Do not commit .env or myenv/ to GitHub. Ensure your .gitignore includes them.

Currently uses GPT-3.5-turbo; you can switch models in blog_state.py.

Large outputs may take some time to generate depending on OpenAI response speed.

🤝 Contributing

Fork the repository

Create a new branch: git checkout -b feature/my-feature

Make your changes and commit: git commit -m "Add feature"

Push to your branch: git push origin feature/my-feature

Open a Pull Request on GitHub

📜 License

This project is licensed under the MIT License. See the LICENSE
 file for details.

📬 Contact

GitHub: Suchitra-Majumdar

Email: asksuchi2015@gmail.com


---

✅ **Why this README works well**

- Gives a **clear overview** of the project and tech stack.  
- Explains **setup**, **usage**, and **project structure** clearly.  
- Includes badges, contribution instructions, and notes for safety.  
- Professional, neat, and easy to read.  

---

If you want, I can also **add GIF/screenshots placeholders** in the README so it looks **more like a polished, portfolio-ready project**.  

Do you want me to do that?




   
   
