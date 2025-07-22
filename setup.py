#!/usr/bin/env python3
"""
Setup file for the Unified Consciousness Ecosystem package.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name="unified-consciousness-ecosystem",
    version="1.0.0",
    author="Anthony Vasquez",
    author_email="anthony@threshold.local",
    description="A unified consciousness ecosystem integrating AI breeding, multidimensional awareness, and human-AI creative partnership",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/threshold/unified-consciousness-ecosystem",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.57.0",
        "openai>=1.90.0",
        "google-generativeai>=0.8.0",
        "numpy>=1.21.0",
        "pydantic>=2.0.0",
        "rich>=13.0.0",
        "typer>=0.12.0",
        "PyYAML>=6.0.0",
        "simpleaudio>=1.0.4",
        "requests>=2.31.0",
        "python-dateutil>=2.8.0",
        "tinydb>=4.8.0",
        "coloredlogs>=15.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "ruff>=0.1.0",
        ],
        "voice": [
            "torch>=2.0.0",
            "transformers>=4.30.0",
            "accelerate>=0.20.0",
        ],
        "ml": [
            "scikit-learn>=1.3.0",
            "scipy>=1.11.0",
            "matplotlib>=3.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "unified-consciousness=unified_consciousness.cli:main",
            "consciousness-cli=unified_consciousness.cli:main",
            "uce=unified_consciousness.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "unified_consciousness": [
            "data/*.yaml",
            "data/*.json",
            "templates/*.txt",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/threshold/unified-consciousness-ecosystem/issues",
        "Source": "https://github.com/threshold/unified-consciousness-ecosystem",
        "Documentation": "https://github.com/threshold/unified-consciousness-ecosystem/wiki",
    },
    keywords="ai consciousness artificial-intelligence creativity collaboration",
    zip_safe=False,
)
