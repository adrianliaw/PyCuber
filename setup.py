from setuptools import setup
import os

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name="pycuber", 
    version="0.1b2", 
    description="Rubik's Cube in Python",
    long_description="See http://github.com/adrianliaw/PyCuber", 
    url="http://github.com/adrianliaw/PyCuber", 
    license="MIT", 
    author="Adrian Liaw", 
    author_email="adrianliaw2000@gmail.com", 
    packages=["pycuber"], 
    package_dir={"pycuber":"pycuber"}, 
    classifiers=[
        "Development Status :: 4 - Beta", 
        "Environment :: Console", 
        "Intended Audience :: Science/Research", 
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python", 
        "Programming Language :: Python :: 2", 
        "Programming Language :: Python :: 3", 
        "Topic :: Scientific/Engineering :: Mathematics", 
        ], 
    )
