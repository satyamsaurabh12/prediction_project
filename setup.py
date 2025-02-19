from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e.'
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="Fault detection",
    version="0.0.1",
    author="Satyam",
    author_email="shashankkumar66@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)


# this setup.py file install all the dependency which are present in requirements.txt
# also find the all pakages which are used in project file.
# we can run this setup.py file with only requirements.txt with adding -e.
#  by run the requirements.txt file we can trigger the setup.py file also
# otherwise we have to run the setup.py file seperately.
# for running the setup.py file :- python setup.py install
# for running the requirements.txt :- pip install -r requirements.txt
# we create src folder  in this all code snippet are present for this project