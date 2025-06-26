# End-to-End-ML-Pipeline

## How to run this project?

conda create -n "env_name" python=3.11 -y

conda activate "env_name"

pip3 install -r requirements.txt

## How to create the project

>> Create the predection pipeline to predict the data user has entered.
>> Now create the user-interface using flask in app.py.

## Project workflow

1. Update config.yaml
2. Update schema.yaml
3. update params.yaml
4. update the entity in src entity
5. update the configuration manager in src config
6. update the components (components like data_injestion, data_validation, etc)
7. update the pipeline in src pipeline
8. update the main.py
9. Update the app.py 

## How to run the project directly from main.py

1. Activate the virtual env.
2. python3 main.py

## How to run the project with the web interfact.

1. Activate the virtual env.
2. python3 app.py

