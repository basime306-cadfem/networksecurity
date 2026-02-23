
"""
The setup.py file is an essential part of packaging and distributing python Projects, It is used by setup tools to define the configuration
of your project, such as metadata dependencies and more.
"""
from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of all the requirements
    """
    requirements:List[str] = []
    try:
        with open('requirements.txt', 'r') as f:
            #Read lines
            lines = f.readlines()

            #Process each line
            for line in lines:
                requriement = line.strip()

                if requriement!='-e .':
                    requirements.append(requriement)

    except:
        print("No Requirement found")

    return requirements


setup(
    name = "NetworkSecurity",
    version="0.1",
    author="Basim",
    packages=find_packages(),
    install_requires=get_requirements()
)



                    



