# Qiskit Project

# Setup for developement:

- Setup a python 3.x venv (usually in `.venv`)
  - You can run `. ./scripts/create-venv.sh` to generate one
- `python -m ensurepip --upgrade`
- `python -m pip install --upgrade setuptools pip`
- `pip3 install --upgrade pip setuptools wheel`
- Install pip-tools `pip3 install pip-tools`
- `pip install numpy==1.26.4`
- `pip install qiskit`
- Update dev requirements: `pip-compile --output-file=requirements.dev.txt requirements.dev.in`
- Update requirements: `pip-compile --output-file=requirements.txt requirements.in`
- Install dev requirements `pip3 install -r requirements.dev.txt`
- Install requirements `pip3 install -r requirements.txt`
- `pre-commit install`

## Update versions

`pip-compile --output-file=requirements.dev.txt requirements.dev.in --upgrade`
`pip-compile --output-file=requirements.txt requirements.in --upgrade`

# Run `pre-commit` locally.

`pre-commit run --all-files`

# Git environment commands

- git config --global --unset user.name
- git config --global --unset user.email
- git config --global user.name "cmalik3595"
- git config --global user.email "cmalik3595@sdsu.edu"
- git config --global push.autosetupremote "true"

- eval "$(ssh-agent -s)"
- ssh-add ~/.ssh/id_rsa
- cat ~/.ssh/id_rsa.pub
- Add ssh key to repository in github
- git remote set-url origin git@github.com:cmalik3595/qsjcm.git
- git push

