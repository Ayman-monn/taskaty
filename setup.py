from setuptools import setup 

setup(
    name='taskaty',
    version='0.1.0', 
    description='A Simple commend-line Task-app written in Python',
    author='Ayman Mohamed', 
    install_requires=['tabulate'],
    entry_points={
        'console_scripts':[
            'taskaty=taskaty:main'
        ]
    }
)