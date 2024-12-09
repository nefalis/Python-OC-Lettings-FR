## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).


La documentation concernant le développement de l'application est accessible via l'url: https://oc-lettings-project.readthedocs.io/en/latest/index.html

Vous pouvez consulter l'application a l'adresse suivante : https://python-oc-lettings-fr-sry9.onrender.com/

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement de OC Lettings Site repose sur un pipeline CI/CD configuré avec GitHub Actions et Docker pour automatiser le processus de développement et de mise en production.

Étapes principales du déploiement :

#### Déclenchement automatique :
- Le pipeline est déclenché automatiquement lors d’un push ou d’une pull request sur les branches master et develop.
- Le déploiement sur le serveur se fait uniquement à partir de la branche master après la réussite des tests.

### Phases du pipeline CI/CD :

#### 1 -Build et vérification du code :
- Les dépendances Python sont installées.
- Des vérifications de style et de qualité (via flake8) sont effectuées.

#### 2-  Exécution des tests unitaires :
- Les tests unitaires sont exécutés avec pytest pour s’assurer que le projet est fonctionnel.
- Un rapport de couverture de test est généré (et doit dépasser 80 % pour réussir).

#### 3- Containerisation de l'application :
- Si les étapes précédentes réussissent, une image Docker est construite et taguée.
- L’image est ensuite poussée sur Docker Hub avec deux tags : un tag basé sur le hash du commit et un tag latest.

### Configuration requise :

- Un compte Docker Hub avec les identifiants configurés comme secrets (DOCKER_USERNAME et DOCKER_PASSWORD) dans le dépôt GitHub.
- Une clé secrète pour l'application (SECRET_KEY) définie dans les secrets GitHub.
- Un compte Render.
- Un compte Docker Hub.

### Étapes nécessaires pour effectuer le déploiement :
