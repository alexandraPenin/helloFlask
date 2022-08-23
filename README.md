# helloFlask
Mon second projet OOP
# Installation et utilisation de Pyenv

sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

pyenv install 3.8.6
pyenv virtualenv 3.8.6 helloFlask
pyenv virtualenvs
pyenv local 3.8.6
pyenv activate helloFlask


curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry new hello_flask

# Tree du projet

├── hello_flask
│   ├── __init__.py
│   └── hello_flask.py
├── poetry.lock
├── pyproject.toml
├── README.rst
└── tests
    ├── __init__.py
    └── test_hello_flask.py


