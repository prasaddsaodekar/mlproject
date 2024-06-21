from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_req(file_path:str)->List[str]:
    '''
    this will return list if req
    '''
    req=[]
    with open(file_path) as file_obj: # requirements.txt
        req = file_obj.readlines()
        req = [r.replace('\n','') for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author='Prasad Saodekar',
    author_email='prasadasaodekar@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')  # ['pandas','numpy','seaborn']
)