#!/bin/bash

pip-compile ./dev_requirements.in --resolver=backtracking
pip install -r ./dev_requirements.txt