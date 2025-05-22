import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "Text Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",  
    "config/config.yaml",                          
    "params.yaml",                                 
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"                        
]

for file_path_str in list_of_files:
    filepath = Path(file_path_str).resolve()
    filedir = filepath.parent

    # Create directory if it doesn't exist
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    else:
        logging.info(f"Directory already exists: {filedir}")

    # Check file
    if filepath.exists():
        if filepath.stat().st_size == 0 and filepath.name != ".gitkeep":
            filepath.write_text("New content for empty file\n")
            logging.info(f"Replaced empty file: {filepath}")
        else:
            logging.info(f"File is not empty: {filepath}")
    else:
        with open(filepath, "w") as f:
            if filepath.name != ".gitkeep":
                f.write("New file created\n")
        logging.info(f"File created: {filepath}")
