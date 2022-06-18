from setuptools import find_packages, setup
from typing import List

PROJECT_NAME="housing_predictor"
VERSION="0.0.2"
AUTHOR="ALOK"
DESCRIPTION="This is my first ML PROJECT"
REQUIREMENT_FILE_NAME='requirements.txt'


def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requiremnts_file:
        return requiremnts_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION ,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

if __name__=='__main__':
    print(get_requirements_list())