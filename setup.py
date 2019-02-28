#!/usr/bin/env python2

import os

from gdpsetuptools import init_gdp_setup
from setuptools import find_packages, setup


DEFAULT_NAME = "clustering_gdp"
file_path = os.path.dirname(__file__)

gdp_details = init_gdp_setup(
    file_path,
    DEFAULT_NAME,
    requirements_file="requirements.txt",
    project_files_path="src/projects",
    )

setup(
    name=gdp_details["module_name"],
    version=gdp_details["version"],
    description="Clustering GDP Projects",
    author="ML Engineering Team",
    author_email="productdelivery.datadiscovery.datascience.dataengineering@grubhub.com",
    url="https://github.com/GrubhubProd/clustering_gdp",
    package_dir={"": "src/python"},
    data_files=gdp_details["data_files"],
    packages=find_packages("src/python"),
    install_requires=gdp_details["requirements"],
    )
