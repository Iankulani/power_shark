#!/usr/bin/env python3
"""
POWER-SHARK Setup Script
"""

from setuptools import setup, find_packages
import os

# Read README
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "POWER-SHARK - Cyber Command Platform"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f 
                    if line.strip() and not line.startswith('#')]
    return []

setup(
    name="power-shark",
    version="1.0.0",
    author="Ian Carter Kulani, MSc",
    author_email="",
    description="Cyber Command & Control Platform - 200+ Security Commands",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/power-shark/power-shark",
    py_modules=["power_shark", "requirements_check"],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "full": [
            "discord.py>=2.3.0",
            "telethon>=1.30.0",
            "slack-sdk>=3.23.0",
            "reportlab>=4.0.0",
            "whois>=0.9.27",
            "qrcode>=7.4.2",
            "pyshorteners>=1.0.1",
            "beautifulsoup4>=4.12.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "power-shark=power_shark:main",
            "power-shark-check=requirements_check:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="security cybersecurity pentesting network-scanner osint",
    project_urls={
        "Bug Reports": "https://github.com/power-shark/power-shark/issues",
        "Source": "https://github.com/power-shark/power-shark",
    },
)
