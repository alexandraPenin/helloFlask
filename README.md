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

# PYENV => sert à installer au tout début une version de python qui sera utilisée par la suite
# LIST DES COMMANDES
pyenv install (--list)
#pyenv virtualenv 3.10.6 nom_du_nouvel_env
pyenv activate nom _du_nouvel_env
pyenv virtualenvs
pyenv versions
pyenv shell
pyenv global nom_du_nouvel_env
pyenv local



# PERMETS DE CREER UNE STRUCTURE TRANSPARENTE + CREE UN ENVIRONNEMENT
# A AUCUN MOMENT ON A BESOIN DE SAVOIR OU VA LA LIBRARY - FAIT JUST POETRY ADD - TOUT EST DANS LE WHEEL LA ROUE
# poetry -> gestion de l'environnement virtuel
#        -> arborescence du projet
#        -> gestion des dépendances (et conflit de dépendances et verbeux explique les dépendances en conflits)
#        -> packaging
# LIST DES COMMANDES
poetry new nom-projet # tiret du milieu très important, en minuscule
poetry add [ou remove] nom_du_packet
poetry shell -> puis python script.py // identique
poetry run [python / count / ...] -> puis python script.py // identique
poetry install # rajoute dans le fichier .locl les dépendances versions
poetry build # crée un dossier dist/ dans lequel il y aura un wheel, un pack reproductible et installable et un fichier tar.gz 





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



from flask import Flask # import de l’objet Flask
app = Flask(__name__) # instantiation application
@app.route("/") # association d’une route (URL) avec la fonction ‘home()’
def home():
return "<p>Bienvenue chez moi</p>" # on renvoie une chaîne de caractères
app.run() # démarrage de l’application




