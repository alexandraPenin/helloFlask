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
├── README.md
└── tests
    ├── __init__.py
    └── test_hello_flask.py


# Installation et utilisation de Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
nano -w ~/.bashrc # rajouter dans son dossier la phrase
poetry --version

cd ~/Documents/
poetry new cow-counts
cd cow-counts
touch cow_counts/mycow.py
poetry add cowsay
poetry new cow-counts # crée une structure de dossier type

poetry install
poetry run count Hello World
poetry build
tree ~/Documents/cow-counts/dist

cd ~/Documents/helloFlask
poetry init --no-interaction

pip install cow_counts-0.1.0-py3-none-any.whl # se positionner dans le dossier du wheel et dans son nouvel environnement, installer le wheel
count Hello World


