#!/bin/bash

isort ./server
black ./server
pylint ./server --rcfile ./server/pylint.rc