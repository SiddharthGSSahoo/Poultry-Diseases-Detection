import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

Project_Name="Poultry-Diseases-Detection-using-CNN"

List_of_Files=[
    ".github/workflows/.gitkeep",
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/components/__init__.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/config/__init__.py",
    f"src/{Project_Name}/config/configuration.py",
    f"src/{Project_Name}/pipeline/__init__.py",
    f"src/{Project_Name}/entity/__init__.py",
    f"src/{Project_Name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for Filepath in List_of_Files:
    Filepath=Path(Filepath)
    Filedir,Filename=os.path.split(Filepath)

    if Filedir!="":
        os.makedirs(Filedir,exist_ok=True)
        logging.info(f"Creating directory: {Filedir} for the file: {Filename}")

    if not os.path.exists(Filepath) or os.path.getsize(Filepath)==0:
        with open(Filepath,'w') as f:
            pass
            logging.info(f"Creating Empty File: {Filepath}")

    else:
        logging.info(f"{Filename} is Already Exists")
     