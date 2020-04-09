import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="hello-world",
    version="v0.2.3",
    author="Alejandro Guzman",
    author_email="",
    description="An example hello world app",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points = {
        'console_scripts': ['hello-world=helloworld.app:main'],
    },
    python_requires=">=3.7"
)