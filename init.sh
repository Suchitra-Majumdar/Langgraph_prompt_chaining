# 1. Create project structure
echo "📂 Setting up project structure..."

mkdir -p app
touch app/__init__.py
touch app/main.py

mkdir -p drafts
mkdir -p graphs
touch .env

# touch drafts/test.ipynb

# mkdir -p .github
# touch .github/deploy.yml


mkdir -p app/config
touch app/config/__init__.py
touch app/config/config.py

mkdir -p app/ui
touch app/ui/__init__.py
touch app/ui/ui.py

mkdir -p app/workflow
touch app/workflow/__init__.py
touch app/workflow/graph_builder.py
touch app/workflow/states.py
touch app/workflow/nodes.py

# mkdir -p app/graph_builder
# touch app/graph_builder/__init__.py
# touch app/graph_builder/graph_builder.py

# mkdir -p app/pdf_generator
# touch app/pdf_generator/__init__.py
# touch app/pdf_generator/pdf_generator.py

mkdir -p app/tests
touch app/tests/__init__.py
touch app/tests/test_graph.py

touch Dockerfile

# Write Dockerfile content
cat > Dockerfile << 'EOF'
FROM python:3.12-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Add the current directory to Python path
ENV PYTHONPATH=/app

# Expose port
EXPOSE 8000

# Run the application
CMD ["streamlit", "run", "app/mainapp.py", "--server.port=8000", "--server.address=0.0.0.0"]
EOF

echo "Dockerfile created successfully"

# 4. Create requirements.txt if not exists & add libraries
if [ ! -f "requirements.txt" ]; then
    echo "📄 Creating requirements.txt..."
    cat <<EOL > requirements.txt
ipykernel
langgraph
langchain
langchain-openai
python-dotenv
dotenv
streamlit
pillow
EOL
    echo "✅ requirements.txt created with default libraries."
else
    echo "📄 requirements.txt already exists, skipping creation."
fi

set -e  # Exit if any command fails

echo "🚀 Initializing Langgraph Prompt Chaining project with Conda..."
conda create --prefix ./venv python=3.12 -y

# 1. Create Conda environment in local folder (./venv)
if [ ! -d "venv" ]; then
    echo "📦 Creating Conda environment in ./venv ..."
    conda create --prefix ./venv python=3.12 -y
else
    echo "✅ Conda environment already exists in ./venv"
fi

echo "🚀 Creating setup.py file with the Project information as needed..."
touch setup.py

# Create setup.py
echo "📝 Creating setup.py..."
cat > setup.py <<EOL
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
EOL

echo "✅ Setup complete and ready to run!"

echo "✅ Project structure is ready."

echo "⚙️  Installing project in editable mode..."
pip install -e .

#Run the file using the command as ./init.sh in gitbash terminal