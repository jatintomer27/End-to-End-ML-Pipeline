# It is the file for ceating project template.

# Execute that file and create the complete folder structure.

## Import the libraries

import os
from pathlib import Path
import logging


## Set the logging configuration

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


# Project root folder

project_name = 'WineProject'


# List files and folder want to create inside directory

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]


# Now Create the all the files and folders required

# Run this file to create the complete project structure 

for file in list_of_files:
    filepath = Path(file) #It will handle which OS we are using and convert this string into that OS path 
    filedir , filename = os.path.split(filepath) # it will split dir and file

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")
