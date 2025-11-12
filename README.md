# End-to-End-ML-Pipeline

## How to run this project?

```bash
conda create -n "env_name" python=3.11 -y
```

```bash
conda activate "env_name"
```

```bash
pip3 install -r requirements.txt
```

## Steps to create the project

01) Create the Github repository and clone it.
02) Create the conda env and active it
03) Create the template.py to create the project structure
04) Update the requirements.txt and install it.
05) Create the project as the package using the pyproject.toml file
06) Write the logging component for the package
07) Update the config/config.yaml file
08) Update the schema.yaml file  ==> According to the DSA (Data sharing agreement)
09) Update the params.yaml file
10) Update the src/project_name/constants
11) Update the src/project_name/utils

12) Update the src/project_name/entity/config_entity.py          =====> Done in Notebook first and if working convert in into project modular
13) Update the src/project_name/config/configuration.py          =====> Done in Notebook first and if working convert in into project modular
14) Update the src/project_name/components/data_ingestion.py     =====> Done in Notebook first and if working convert in into project modular
15) Update the src/project_name/pipeline/data_ingestion.py       =====> Done in Notebook first and if working convert in into project modular

16) Update the main.py   ===> From here all the things are tested and worked

17) Like this we will do for all the steps ( Data ingestion, Data Validation, Data Transformation , Model Trainer , Model Evaluation )

18) Create the prediction pipeline 
	==> Create the file src/<project_name>/pipeline/prediction.py

19) Create the user interface ( app ) 
	==> We will use flask to create the user app
	==> Create the app.py
	
20) Run the project from app.py

## How to run the project directly from main.py

1. Activate the virtual env.
2. python3 main.py

## How to run the project with the web interfact.

1. Activate the virtual env.
2. python3 app.py


# AWS-CICD-Deployment-with-Github-Actions

[Github Actions CI/CD Deployment](https://github.com/jatintomer27/MLOps/blob/main/class_10.md)

