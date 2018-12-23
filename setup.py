import os
from setuptools import setup, find_packages

setup(
    name = 'backgammon',
    version = '0.1.0',
    description = 'TD-gammon implementation',
    author = 'Daniel Roythorne',
    author_email = 'dan@droythorne.com',
    url = 'https://droythorne.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires = [
    ],
    entry_points = {
        'console_scripts': [
        ]
    }
)
