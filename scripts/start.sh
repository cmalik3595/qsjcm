#!/bin/sh
#
. ./scripts/create-venv.sh
python -m ensurepip --upgrade
python -m pip install --upgrade setuptools pip
pip3 install --upgrade pip setuptools wheel
pip3 install pip-tools

pip-compile --output-file=requirements.txt requirements.in
pip3 install -r requirements.txt

#- pip install numpy==1.26.4
#- pip install qiskit
#- Update dev requirements: pip-compile --output-file=requirements.dev.txt requirements.dev.in`
#- Update requirements: pip-compile --output-file=requirements.txt requirements.in`
#- Install dev requirements pip3 install -r requirements.dev.txt`
#- Install requirements pip3 install -r requirements.txt
