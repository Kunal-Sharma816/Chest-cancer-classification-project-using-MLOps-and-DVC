import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ChestCancerClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",  # Fixed: pipeline spelling
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",  # Fixed: constants spelling
    "config/config.yaml",  # Fixed: yaml spelling
    "dvc.yaml",            # Fixed: yaml spelling
    "params.yaml",         # Fixed: yaml spelling
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # FIX: Write to the full filepath
            pass
        logging.info(f"Creating empty file: {filepath}")  # FIX: Proper f-string
    else:
        logging.info(f"{filename} already exists")
