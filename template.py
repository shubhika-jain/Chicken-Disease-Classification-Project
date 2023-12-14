import os
from  pathlib import Path 
import logging

#logging everything
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')
project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src{project_name}/__init__.py", #to install as a local package
    f"src{project_name}/components/__init__.py",
    f"src{project_name}/utils/__init__.py",
    f"src{project_name}/config/configurations.py",
    f"src{project_name}/pipeline/__init__.py",
    f"src{project_name}/entity/__init__.py",
    f"src{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "reqirements.txt",
    "setup.py",
    "research/trials.pynb"
]

for filepath in list_of_files:
    filepath= Path(filepath)        #it  converts into the filepath type used in the os
    filedir, filename = os.path.split(filepath) #returns folder and files created in os

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} fr the file {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
    
