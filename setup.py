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


"""
## What the line package_dir={"": "src"} is doing ?

- This tells setuptools that the root directory of your packages is src/, 
    not the root of the project 

- By default, setuptools looks for packages in the same directory as setup.py. 

- But many developers prefer to keep their source code isolated in a folder like src/ to avoid issues.

### 🧠 How it works:

- The empty string "" refers to the current directory where setup.py is located.

- "src" says: when looking for packages relative to "", actually look in the src/ directory.
"""


"""
## What the line packages=find_packages(where="src") is doing ?

- This automatically finds all Python packages (i.e., folders with an __init__.py file) 
  inside the src/ directory


### 🧠 How it works:

- find_packages(where="src") searches inside src/ for all valid Python packages and returns them as a list.

- It uses the __init__.py file to recognize a package.
 
"""