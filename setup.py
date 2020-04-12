from setuptools import setup, find_packages
import json

requirements = open('requirements.txt').read().splitlines()

project = json.load(open('project.json'))

setup(
    name=project['name'],
    version=project['version'],
    author=project['author'],
    author_email=project['author_email'],
    description='An example hello world app',
    long_description=open('README.md').read(),
    url='https://github.com/alejandro-guzman/hello-world',
    license='MIT',
    keywords='flask api example',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['hello-world=helloworld.app:main'],
    },
    project_urls={
        'Source Code': 'https://github.com/alejandro-guzman/hello-world',
    },
    python_requires='>=3.7'
)