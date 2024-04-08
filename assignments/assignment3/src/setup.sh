#!/usr/bin/bash

python -m venv envLang3

source ./envLang3/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

deactivate