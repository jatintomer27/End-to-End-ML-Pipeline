from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version = "1.0.0"

REPO_NAME = "ML_pipeline"
AUTHOR_USER_NAME = "jatin"
SRC_REPO = "ML_pipeline"
AUTHOR_EMAIL = "jatintomer27@gmail.com"

setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"}, 
    packages=find_packages(where="src"),
    install_requires=[], 
)

"""
## What this packages will do?

## It will find the __init__.py file.

## And install this as local package.
"""