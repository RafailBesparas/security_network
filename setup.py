## Essential file for package distribution
## It is used to setup tools, define configurations, such as metadata, dependencies and more

from setuptools import find_packages, setup
from typing import List

# read the requirement txt file and return the list of requirements
def get_requirements() ->  List[str] :
    """ This function will return list of requirements"""

    #initialize the requirement list as an empty list of strings 
    requirement_lst: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file 
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e.
                # install all the other packages except the -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement) # add to this list all the requirements 
    except FileNotFoundError:
        print("requirements.txt file not found in the system")
    
    return requirement_lst


setup (
    name = "Network Security Project Extension",
    version= "0.0.1",
    author = "Krish Naik",
    email = "emotional_support@python.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

print(get_requirements())