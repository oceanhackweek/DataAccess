import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "isopy",
    version = "0.0.1",
    author = "Laura Gruenburg, Tongya Liu, Shanice Bailey, Kexin Song",
    author_email = "lkg2133@columbia.edu",
    description = ("Functions for determining variables along isopycnal surfaces from standard depths"),
    license = "BSD-3-Clause",
    keywords = "function, example",
    url = "https://github.com/oceanhackweek/DataAccess/tree/master/isopy",
    packages=['isopy'],
    long_description=read('README'),
    classifiers=[
        "License :: OSI Approved :: BSD-3-Clause License",
    ],
)
