'''
This is a setup.py file for a Python package.
It includes 
- Metadata about the package such as its name, version, author, and description.
- Dependenies required for the package to run.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads a requirements file and returns a list of dependencies.
        
    Returns:
        List[str]: A list of dependencies.
    """
    requirment_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirment = line.strip()
                if requirment and not requirment.startswith('#') and requirment != "-e .":
                    requirment_lst.append(line)        
    except FileNotFoundError:
        print(f"Warning: requirements.txt not found. No dependencies will be installed.")
    return requirment_lst

setup(
    name='MLOPS PROJECT',
    version='0.0.1',
    author='Abhishek Raj Chowdary', 
    author_email= 'arc11832811@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    )
