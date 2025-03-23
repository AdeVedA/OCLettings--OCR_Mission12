![OrangeCountyLettings_Ad](https://user.oc-static.com/upload/2023/07/20/1689880374259_Orange%20County%20Lettings%20Ad.png)


<h1 align="center">
    <img src="static/assets/img/logo.png" width="50" 
         style="background: white; border-radius: 50%; padding: 5px;">
    <b>OC Lettings</b> - Plateforme de locations
</h1>

<div align="center">

  |      Site     |  Image Docker | Documentation |
  |---------------|---------------|---------------|
  | [OC-Lettings](https://oc-lettings-yua5.onrender.com/) | [DockerHub](https://hub.docker.com/repository/docker/adeveda/oclettings/general) | [ReadTheDocs](https://oclettings-ocr-mission12.readthedocs.io/fr/latest/index.html) |

</div>

## <img src="https://img.icons8.com/color/48/home--v1.png" width="30"> Présentation

**OC Lettings** est une **application Web Django** d'Orange County Lettings permettant de lister des *locations immobilières* et de présenter les *profils utilisateurs*.
À partir d'un fork d'une version "beta", la mission était :
- **refactorer** un projet django en **trois applications** (*architecture modulaire*, *migration des données* et gestion restructurée des *templates et URLs*)
- Correction de **bugs**, amélioration du **linting**,
- Gestion des **erreurs 404 et 500** (avec pages aux *images personnalisées*),
- Écriture des **tests unitaires et d'intégration**,
- **Docstrings et documentation** complète.
- Détection et suivi/monitoring centralisé des erreurs avec logs structurés via **Sentry**.
- Mise en place d'un **pipeline CI/CD** et **déploiement** :
  - validation du **linting** flake8 et des **tests** pytest (pour une couverture supérieure à 80%),
  - **build Docker** et push de l'image versionnée sur **DockerHub**,
  - **déploiement** sur Render.
- Génération de la **documentation** via Sphinx et déploiement sur Read the Docs.


## 🏗️ Architecture

- **Applications Django** : 
  - `lettings` : Gère les annonces immobilières et leurs adresses
  - `profiles` : Gère les profils utilisateurs liés aux comptes Django
- **Base de données** : SQLite par défaut, configurable via variables d'environnement
- **Outils** :
  - Sentry pour le monitoring des erreurs
  - Docker pour la mise en production
  - GitHub Actions pour le CI/CD

### 🔄 Pipeline CI/CD
1. Tests automatisés (flake8 + pytest) sur chaque push sur `main`
2. Build de l'image Docker si les tests réussissent
3. Push de l'image Docker vers Docker Hub
4. Déploiement automatique sur Render grâce à un hook configuré dans GitHub Secrets

---

## ⚙️ Installation

### <img src="https://img.icons8.com/color/48/checklist.png" width="30"> Prérequis
- Python 3.12+ ([Windows](https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe) ou [Mac](https://www.python.org/ftp/python/3.12.9/python-3.12.9-macos11.pkg))
- Git pour [Windows](https://github.com/git-for-windows/git/releases/download/v2.49.0.windows.1/Git-2.49.0-64-bit.exe) ou pour Mac :
  - install Homebrew :
    ```bash
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    $ brew install git
    ```
- Docker (pour la pré-production) ([Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_location=module) ou [Mac](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_location=module))

en local :
  - variables d'environnement dans un fichier `.env`

en prod :
  - un compte GitHub avec un fork de ce projet
  - variables d'environnement définis en github secrets

### <img src="https://img.icons8.com/color/48/windows-10.png" width="30"> Configuration Windows
1. Cloner le repository:
```bash
  cd chemin\pour\mettre\le\project
  git clone https://github.com/AdeVedA/OCLettings--OCR_Mission12.git
  cd OCLettings--OCR_Mission12
```
2. Créer et activer l'environnement virtuel:
```bash
  python -m venv venv
  venv\Scripts\activate
```
3. Installer les dépendances dans cet environnement activé:
```bash
  pip install -r requirements.txt
```
4. Configurer les variables d'environnement dans un fichier à la racine du projet `.env` :
```ini
  # Django settings
  DEBUG=False
  SECRET_KEY="votre secret_key django"
  ALLOWED_HOSTS=localhost,127.0.0.1,{votre nom de domaine de production}
  DJANGO_CSRF_TRUSTED_ORIGINS=https://localhost:8000,{votre url de production}

  # Database settings
  DATABASE_ENGINE='sqlite3'
  DATABASE_NAME='oc-lettings-site.sqlite3'

  # Sentry DSN
  SENTRY_DSN='{votre dsn sentry pour le projet}'
```
5. Migrations & lancement du serveur :
```bash
  python manage.py migrate
  python manage.py runserver
```
6. Aller sur `http://localhost:8000` dans un navigateur.
### <img src="https://img.icons8.com/color/48/linux.png" width="30"> <img src="https://img.icons8.com/color/48/mac-os.png" width="30"> Configuration Linux/MacOS
```bash
# Créer le dossier et cloner le repo
  cd /path/to/project/folder
  git clone https://github.com/AdeVedA/OCLettings--OCR_Mission12.git
  cd OCLettings--OCR_Mission12

# Créer et activer l'environnement virtuel
  python3 -m venv venv
  source venv/bin/activate

# Installation des dépendances
  pip install -r requirements.txt

# Créer et configurer le fichier .env
  (voir le point 4. de la config. windows)

# Migrations & lancement du serveur
  python manage.py migrate
  python manage.py runserver

# Aller sur `http://localhost:8000` dans un navigateur.
```

#### <img src="https://img.icons8.com/color/48/checked-2.png" width="30"> Linting & Tests unitaires

- Mettez-vous à la racine du projet, activez l'environnement virtuel puis :
- pour le linting :
```bash
  `flake8`
```
- pour les tests unitaires :
```bash
- `pytest`
```

#### <img src="https://img.icons8.com/color/48/control-panel.png" width="30"> Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

---

## <img src="https://img.icons8.com/color/48/docker.png" width="30"> Utilisation de Docker

### 💻 Environnement local
```bash
# Construire l'image avec vos variables (ex: SECRET_KEY_DJANGO)
docker build --build-arg SENTRY_DSN="${{ secrets.SENTRY_DSN }}" \
             --build-arg SECRET_KEY_DJANGO="${{ secrets.SECRET_KEY_DJANGO }}" \
             -t "${{ secrets.DOCKER_IMAGE_NAME }}:${{ github.sha }}" .

# Exécuter le conteneur
docker run -p 8000:8000 \
           -e SECRET_KEY="votre_clé" \
           -e SENTRY_DSN="votre_sentry_dsn" \
           oclettings:latest
```

### <img src="https://img.icons8.com/color/48/server.png" width="30"> Production
- déclarez l'ensemble de ces variables dans votre GitHub Secrets Actions:
DOCKERHUB_PASSWORD, DOCKERHUB_USERNAME, DOCKER_IMAGE_NAME, RENDER_HOOK, SECRET_KEY_DJANGO, SENTRY_DSN

Le workflow GitHub (`.github\workflows\main.yaml`) gèrera alors automatiquement le déploiement :
1. Les commits vers la branche `main` déclenchent les tests
2. Si réussis, une nouvelle image Docker est construite et publiée sur votre Docker Hub
3. Le hook Render est activé pour re-déployer automatiquement

---

## <img src="https://img.icons8.com/color/48/rocket.png" width="30"> Déploiement 

### <img src="https://img.icons8.com/color/48/numbered-list.png" width="30"> Récapitulatif des étapes
1. **Tests** : Vérification du code (flake8) et exécution des tests unitaires avec couverture minimale de 80%
2. **Build Docker** : Création d'une image contenant l'application
3. **Push sur Docker Hub** : Stockage de l'image créée sur DockerHub
4. **Déclenchement Render** : Un hook Render pour déployer la nouvelle version

### ⚠️ Configuration requise
- Compte Docker Hub avec accès en écriture pour le repository configuré
- Accès à Sentry (variable `SENTRY_DSN`)
- Hook de déploiement Render disponible dans les secrets GitHub
- Variables d'environnement nécessaires dans votre GitHub Secrets Actions (via *Settings > Secrets and variables*) :
SECRET_KEY_DJANGO
SENTRY_DSN
DOCKERHUB_USERNAME
DOCKERHUB_PASSWORD
DOCKER_IMAGE_NAME
RENDER_HOOK

### <img src="https://img.icons8.com/color/48/package.png" width="30"> Instructions de déploiement
1. **Pré-requis** : 
  - vos secrets GitHub décrits précédemment
2. **Déploiement automatique** :
  - Effectuez un push vers la branche `main`
  - Le workflow GitHub déclenche les étapes de CI/CD
  - Vérifiez le statut des jobs sur [GitHub Actions](https://github.com/[votre_repo]/actions)
3. **Validation post-déploiement** :
  - Accédez à l'URL du serveur Render pour vérifier le fonctionnement

---
