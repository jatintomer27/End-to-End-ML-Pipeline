# End-to-End-ML-Pipeline

## How to run this project?

conda create -n "env_name" python=3.11 -y

conda activate "env_name"

pip3 install -r requirements.txt

## How to create the project

- Create the predection pipeline to predict the data user has entered.
- Now create the user-interface using flask in app.py.

## Steps to create the Project.

1. create template.py
2. Create folder structure using template.py
3. Update the setup.py to make ML_pipeline as package
4. Configure logger in ML_pipeline package.
5. Update the constants and utils in ML_pipeline package

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


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/winerepo

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

