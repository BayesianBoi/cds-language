#!/usr/bin/env bash

# Create a virtual environment
python3 -m venv EnvLang1

# Activate the virtual environment
source EnvLang1/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
