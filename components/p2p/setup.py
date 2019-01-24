import os
from setuptools import setup, find_packages


def parse_requirements(fname):
    """Loads requirements from a pip requirements file with fname"""
    with open(os.path.join(os.path.dirname(__file__), fname)) as fhandle:
        reader = fhandle.readlines()
    return [line for line in reader if line and not line.startswith("#")]


setup(
    name="pandastoproduction",
    version="0.1.0",
    description="Pandas to Production",
    url="https://git.enigma/hackweek/pandas-to-production/p2p",
    author="Enigma Technologies",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    tests_require=parse_requirements("dev-requirements.txt"),
    zip_safe=False,
)
