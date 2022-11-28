
"""Config file to build package."""
from setuptools import find_packages, setup

VERSION = "1.0"
DESCRIPTION = "Forked Daprofiler Tool"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

# Setting up
setup(
    name="daprofiler_tool",
    version=VERSION,
    author="",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/pilotbird-Truphena-Lwanga/DaProfiler",
    project_urls={
        "Original_repo": "https://github.com/daprofiler/DaProfiler",
    },
    packages=find_packages(),
    install_requires=install_requires,
    keywords=[
        "python",
        "daprofiler",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
       
    ],
)