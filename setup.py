# Importing the `find_packages` function to automatically discover all packages and subpackages
# and `setup` function to define the package configuration
from setuptools import find_packages, setup

# Importing List type hint from typing module
from typing import List

# This constant represents a line in requirements.txt that refers to installing the current directory as a package
HYPHEN_E_DOT = '-e .'

# Function to read requirements from a file and return them as a list of strings
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    # Open the file containing requirements
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace('\n', '') for req in requirements]
        # Remove the '-e .' entry if present (used for editable installs)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    # Return the cleaned list of requirements
    return requirements

# The setup function defines the package metadata and dependencies
setup(
    name='mlproject',                        # Name of the package/project
    version='0.0.1',                         # Initial version of the package
    author='brajeshhhhh',                    # Author's name
    author_email='bs6027@srmist.edu.in',     # Author's email
    packages=find_packages(),                # Automatically find and include all packages
    install_requires=get_requirements('requirements.txt')  # List of required dependencies from requirements.txt
)
