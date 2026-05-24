#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="flowcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "flowcli=flowcli.cli:cli",
        ],
    },
)