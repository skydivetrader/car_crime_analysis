from setuptools import setup, find_packages

setup(
    name='car_crime_analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'matplotlib',
        'pandas'
    ],
    author='Your Name',
    description='Module for analyzing car theft and organized crime reports',
)