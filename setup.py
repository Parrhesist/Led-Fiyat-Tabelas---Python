#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="altin-fiyat-tabelasi",
    version="1.0.0",
    author="Mehmet Açıkgöz",
    author_email="mehmetacikgoz8585@gmail.com",
    description="Altın fiyat verilerini LED tabela formatında görüntüleyen uygulama",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Parrhesist/Led-Fiyat-Tabelas---Python",
    project_urls={
        "Bug Reports": "https://github.com/Parrhesist/Led-Fiyat-Tabelas---Python/issues",
        "Source": "https://github.com/Parrhesist/Led-Fiyat-Tabelas---Python",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "altin-tabelasi=main:main",
        ],
    },
    keywords="altın, fiyat, tabela, led, kuyumcu, python, tkinter",
    include_package_data=True,
    zip_safe=False,
)
