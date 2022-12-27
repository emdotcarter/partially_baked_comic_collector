#!/bin/bash

pyenv install -s
pyenv virtualenv $(tail ./.python-version -n 1) $(head ./.python-version -n 1)
pip install pip-tools
