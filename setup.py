#!/usr/bin/env python3
"""
Setup script for DXM Radar Toolkit

This educational toolkit provides a CLI interface for interacting with
Banner DXM wireless controllers and their connected radar sensors via Modbus TCP.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="dxm-radar-toolkit",
    version="1.0.0",
    author="Industrial Automation Engineer",
    author_email="engineer@example.com",
    description="Educational toolkit for Banner DXM radar sensors with comprehensive Modbus integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dxm-radar-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: System :: Hardware",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dxm=dxm_toolkit.cli:cli",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="modbus, radar, sensor, industrial, automation, banner, dxm, education",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/dxm-radar-toolkit/issues",
        "Source": "https://github.com/yourusername/dxm-radar-toolkit",
        "Documentation": "https://github.com/yourusername/dxm-radar-toolkit/docs",
    },
)