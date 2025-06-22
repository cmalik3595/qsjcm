#!/usr/bin/env bash
python3 -m venv qiskit-env
source qiskit-env/bin/activate


python -m ensurepip --upgrade
python -m pip install --upgrade setuptools pip
