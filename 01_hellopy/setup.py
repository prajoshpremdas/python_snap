import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

this = os.path.dirname(os.path.realpath(__file__))

def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()

setuptools.setup(
    name="hellopy",
    version="0.0.1",
    author="Prajosh Premdas",
    author_email="premdas.prajosh@gmail.com",
    description="A small example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['hellopy'],
    install_requires=read('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    scripts=['bin/hellopy'],
    include_package_data=True
)
